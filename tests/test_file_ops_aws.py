import pytest
from moto import mock_s3
import sys
import pandas as pd
import json
sys.path.append('./source')
from file_ops import Aws
from clean_data import Operations
sys.path.append('../tests')
from test_aws_conn import TestConnection
from test_config import TestConfig


class TestFileOpsS3:

    @mock_s3
    def __init__(self):
        config = TestConfig()
        bucket_obj = test_get_bucket_obj(config.bucket, config.output_dir + "data_file" + config.input_ext, os.path.join(os.path.join(os.getcwd(), 'tests'), 'data_file.csv'))
        self.aws_obj = Aws(bucket_obj)

    @mock_s3
    def test_get_file_list(self):
        file_list = self.aws_obj.get_files_list(config.source_dir)
        for current_file in file_list:
            key = current_file.key
        assert key == config.source_dir + "data_file" + config.input_ext

    @mock_s3
    def test_read_file(self):
        data = self.aws_obj.read_file(config.source_dir + "data_file" + config.input_ext)
        data_upload = pd.read_csv(os.path.join(os.path.join(os.getcwd(), 'tests'), 'data_file.csv'))
        csv_object = Operations(data_upload)
        data_desired = csv_object.remove_empty_rows().reset_index(drop=True),
        assert data_desired == data.reset_index(drop=True)

    @mock_s3
    def test_move_file(self):
        self.aws_obj.move_file(config.source_dir + "data_file" + config.input_ext, config.archive_dir + 'data_file.csv')
        file_list = self.aws_obj.get_files_list(config.archive_dir)
        for current_file in file_list:
            key = current_file.key
        assert key == config.archive_dir + "data_file" + config.input_ext

    @mock_s3
    def test_write_file(self):
        output_json = json.dumps('{"sample": "json"}')
        self.aws_obj.move_file(output_json, config.output_dir + "data_file" + config.output_ext)
        file_list = self.aws_obj.get_files_list(config.output_dir)
        for current_file in file_list:
            key = current_file.key
        assert key == config.output_dir + "data_file" + config.output_ext
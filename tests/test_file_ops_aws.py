""" module to test file_ops module """
import os
import json
from moto import mock_s3
import pandas as pd
from source.file_ops import Aws
from source.clean_data import Operations
from tests.test_aws_conn import test_get_bucket_obj
from tests.test_config import TestConfig

class TestFileOpsS3:
    """ class to check all the file_ops function """
    @mock_s3
    def test_get_file_list(self):
        """ Test get list of files in a bucket """
        config = TestConfig()
        bucket_obj = test_get_bucket_obj()
        aws_obj = Aws(bucket_obj)
        file_list = aws_obj.get_files_list(config.source_dir)
        bucket_list = [bucket.key for bucket in file_list]
        assert bucket_list[0] == config.source_dir + "data_file" + config.input_ext

    @mock_s3
    def test_read_file(self):
        """ Test read file to check if the fuction is reading file from s3"""
        config = TestConfig()
        bucket_obj = test_get_bucket_obj()
        aws_obj = Aws(bucket_obj)
        data = aws_obj.read_file(config.source_dir + "data_file" + config.input_ext)
        data_upload = pd.read_csv(os.path.join(os.path.join(os.getcwd(), 'tests'), 'data_file.csv'))
        csv_object = Operations(data_upload)
        data_desired = csv_object.remove_empty_rows().reset_index(drop=True)
        pd.testing.assert_frame_equal(data_desired, data.reset_index(drop=True))

    @mock_s3
    def test_move_file(self):
        """ Test move_file to check if function is moving files between folders """
        config = TestConfig()
        bucket_obj = test_get_bucket_obj()
        aws_obj = Aws(bucket_obj)
        aws_obj.move_file(config.source_dir +
                          "data_file" +
                          config.input_ext, config.archive_dir + 'data_file.csv')
        file_list = aws_obj.get_files_list(config.archive_dir)
        bucket_list = [bucket.key for bucket in file_list]
        assert bucket_list[0] == config.archive_dir + "data_file" + config.input_ext

    @mock_s3
    def test_write_output(self):
        """ Test write_output to check if the fuction is writing output to s3 """
        config = TestConfig()
        bucket_obj = test_get_bucket_obj()
        aws_obj = Aws(bucket_obj)
        output_json = json.dumps('{"sample": "json"}')
        aws_obj.write_output(output_json, config.output_dir + "data_file" + config.output_ext)
        file_list = aws_obj.get_files_list(config.output_dir)
        bucket_list = [bucket.key for bucket in file_list]
        assert bucket_list[0] == config.output_dir + "data_file" + config.output_ext

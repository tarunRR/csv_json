import pytest
from moto import mock_s3
import sys
import pandas as pd
import json
sys.path.append('./source')
from file_ops import Aws
from main import all_operations
from clean_data import Operations
sys.path.append('../tests')
from test_aws_conn import TestConnection
from test_config import TestConfig




def test_all_operations():
    config = TestConfig()
    bucket_obj = test_get_bucket_obj(config.bucket, config.output_dir + "data_file" + config.input_ext, os.path.join(os.path.join(os.getcwd(), 'tests'), 'data_file.csv'))
    aws_obj = Aws(bucket_obj)
    all_operations(config,aws_obj)
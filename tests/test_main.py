""" File to test main function """
from moto import mock_s3
from source.file_ops import Aws
from source.main import all_operations
from tests.test_aws_conn import test_get_bucket_obj
from tests.test_config import TestConfig



@mock_s3
def test_all_operations():
    """ function to test all operations function """
    config = TestConfig()
    bucket_obj = test_get_bucket_obj()
    aws_obj = Aws(bucket_obj)
    all_operations(config, aws_obj)

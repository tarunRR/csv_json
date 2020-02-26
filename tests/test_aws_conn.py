""" Used for creating session and bucket object  """
import os
import boto3
from moto import mock_s3


@mock_s3
def test_get_bucket_obj():
    """
    Function to get bucket object from aws
    """
    conn = boto3.resource('s3', region_name='us-east-1')
    conn.create_bucket(Bucket='buckettest')
    bucket_object = conn.Bucket('buckettest')
    file_path = os.path.join(os.path.join(os.getcwd(), 'tests'), 'data_file.csv')
    bucket_object.upload_file(file_path, "csv/data_file.csv")
    return bucket_object

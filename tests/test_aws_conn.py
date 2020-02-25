import argparse
import boto3
from moto import mock_s3
class TestConnection:
    """
    class for creating session with aws
    """
    @mock_s3
    def test_create_session(self):
        """
        Function to create session with aws
        """
        session = boto3.session.Session()
        return session

    @mock_s3
    def test_get_bucket_obj(self, bucket_name, file_key, file_path):
        """
        Function to get bucket object from aws
        :parameters:
            bucket_name -  name of the bucket folders are stored in
        """
        session_object = self.test_create_session()
        resource_object = session_object.resource('s3')

        # create bucket
        resource_object.create_bucket(bucket_name)

        # Upload file
        resource_object.Object(bucket_name, file_key).put(Body=open(file_path, 'rb'))
        bucket_object = resource_object.Bucket(bucket_name)
        return bucket_object



        

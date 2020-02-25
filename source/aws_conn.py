import argparse
import boto3
class Connection:
    """
    class for creating session with aws
    """
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--access_key_arg')
        parser.add_argument('--secret_key_arg')
        args = parser.parse_args()
        self.access_key = args.access_key_arg
        self.secret_key = args.secret_key_arg

    def create_session(self):
        """
        Function to create session with aws
        """
        if self.access_key and self.secret_key:
            session = boto3.session.Session(
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key
            )
        else:
            session = boto3.session.Session()
        return session

    def get_bucket_obj(self, bucket_name):
        """
        Function to get bucket object from aws
        :parameters:
            bucket_name -  name of the bucket folders are stored in
        """
        session_object = self.create_session()
        resource_object = session_object.resource('s3')
        return resource_object.Bucket(bucket_name)

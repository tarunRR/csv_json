import logging
import pandas as pd
from clean_data import Operations
from exception import S3Error

class Local:

    def __init__(self):
        """
        Initializes the object.
        """
        self.data = None

    def read_data(self, data):
        """
        Directly read data into the object
        :parameters:
            data - data to be processed
        """
        self.data = Operations(data).remove_empty_rows()
        return self.data

    def read_file(self, path):
        """
        Reads path and upload file to data_to_use variable
        :parameters:
            path - absolute/relative path of file to be uploaded
        """
        data = pd.read_csv(path)
        self.data = Operations(data).remove_empty_rows()
        return self.data


class Aws:

    def __init__(self, bucket_object):
        """
        Initializes the object.
        """
        self.bucket_object = bucket_object

    def get_files_list(self, direc):
        """
        Get list of files present in source folder in aws
        :parameters:
            direc - directory to be checked
        """
        try:
            files = self.bucket_object.objects.filter(Prefix=direc)
            logging.info(f'Files present in directory : {files}')
        except Exception as ex:
            raise S3Error(f'Failed to parse the S3 bucket {self.bucket_object} Error:{str(ex)}')
        return files


    def read_file(self, file_key):
        """
        Read file from he location key specified
        :parameters:
            file_key - location key of file to be read
        """
        try:
            csv_object = self.bucket_object.Object(file_key).get()
            data = pd.read_csv(csv_object['Body'])
            logging.info(f'Read file {file_key} into the object')
        except Exception as ex:
            raise S3Error(f'Failed to read source file {file_key} Error: {str(ex)}')
        return Operations(data).remove_empty_rows()

    def move_file(self, src_key, destn_key):
        """
        Move file from one folder to another in a bucket
        :parameters:
            src_key - location key of file to be moved
            destn_key - location key file needs to be moved to
        """
        try:
            csv_source = {'Bucket': self.bucket_object.name, 'Key': src_key}
            destn_object = self.bucket_object.Object(destn_key)
            destn_object.copy(csv_source)
            logging.info(f'moved file from {src_key} to the location {destn_key}')
        except Exception as ex:
            raise S3Error(f'Failed to move file from {src_key} '
                          f'to the location {destn_key} Error: {str(ex)}')

    def delete_file(self, file_key):
        """
        Delete file from a location key
        :parameters:
            file_key - location key of file to be deleted
        """
        try:
            self.bucket_object.Object(file_key).delete()
            logging.info(f'deleted file {file_key}')
        except Exception as ex:
            raise S3Error(f'Failed to delete file {file_key} Error: {str(ex)}')

    def write_output(self, output_var, destn_key):
        """
        Write file to a specific location key
        :parameters:
            output_var - Ouput varible to be written
            destn_key - location key file needs to be written to
        """
        try:
            destn_object = self.bucket_object.Object(destn_key)
            destn_object.put(Body=output_var)
            logging.info(f'saved json output generated from csv to {destn_key}')
        except Exception as ex:
            raise S3Error(f'Failed to save json output generated'
                          f'from csv to {destn_key} Error: {str(ex)}')

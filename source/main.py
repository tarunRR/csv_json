"""
This file is the main file of the code module which calls all the functions and do all the operations
"""
import logging
import traceback
import sys
sys.path.append('./source')
#pylint: disable=wrong-import-position
from configuration import Config
from aws_conn import Connection
from file_ops import Aws
from get_tree import ConvertCsvToJson
from exception import ValidationError, FileNotExist, error_message
#pylint: enable=wrong-import-position

def all_operations(config, aws_obj):
    """
    Run this function to do all the operations at once
    :parameters:
        config - object from configuration.py, contains info from config file
        aws_obj - object that contains aws's session and bucket info
    """
    try:
        files = aws_obj.get_files_list(config.source_dir)
        if not files:
            raise FileNotExist(f'No file exist in {config.s3bucket} '
                               f'and prefix {config.sourcefolder} '
                               f'for file extension {config.infileextension}')
        for current_file in files:
            try:
                if current_file.key.endswith(config.input_ext):

                    # Read file from aws
                    data = aws_obj.read_file(current_file.key)
                    csv_object = ConvertCsvToJson(data)
                    out_json = csv_object.create_tree()

                    # Write output to json folder aws
                    output_key = current_file.key.replace(config.source_dir, config.output_dir)
                    output_key = output_key.replace(config.input_ext, config.output_ext)
                    aws_obj.write_output(out_json, output_key)

                    # Move file to archive
                    move_key = current_file.key.replace(config.source_dir, config.archive_dir)
                    aws_obj.move_file(current_file.key, move_key)

                    # Delete file from source
                    aws_obj.delete_file(current_file.key)

            except Exception as ex:

                # If error in file move to error  directory
                move_key = current_file.key.replace(config.source_dir, config.error_dir)
                aws_obj.move_file(current_file.key, move_key)
                aws_obj.delete_file(current_file.key)
                raise ValidationError(f'File {current_file} content is '
                                      f'not in proper format Error: {str(ex)}')
    except FileNotExist as ex:
        logging.error(error_message(ex.code, ex.message, ex.additionalmessage))
        traceback.print_exc()
    except ValidationError as ex:
        logging.error(error_message(ex.code, ex.message, ex.additionalmessage))
        traceback.print_exc()

if __name__ == '__main__':
    config = Config()
    conn_object = Connection()
    bucket_obj = conn_object.get_bucket_obj(config.bucket)
    aws_obj = Aws(bucket_obj)
    all_operations(config, aws_obj)

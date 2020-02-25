import configparser

class Config:
    """
    Config class to pass variables with respect to each environment
    """
    def __init__(self):
        """
        Init method of Config class
        """
        config = configparser.ConfigParser()
        config.read('./config/aws_config.ini')

        self.source_dir = config.get('aws_data', 'source_dir')
        self.output_dir = config.get('aws_data', 'output_dir')
        self.error_dir = config.get('aws_data', 'error_dir')
        self.archive_dir = config.get('aws_data', 'archive_dir')
        self.input_ext = config.get('aws_data', 'input_ext')
        self.output_ext = config.get('aws_data', 'output_ext')
        self.bucket = config.get('aws_data', 'bucket')
        self.bucket_test = config.get('aws_data', 'bucket_test')

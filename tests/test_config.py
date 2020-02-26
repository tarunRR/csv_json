""" initialises the config object we are going to use later """
class TestConfig:
    """ Classs initialises the config object we are going to use later """
    def __init__(self):
        """ constructor """
        self.source_dir = 'csv/'
        self.output_dir = 'json/'
        self.error_dir = 'error/'
        self.archive_dir = 'archive/'
        self.input_ext = '.csv'
        self.output_ext = '.json'
        self.bucket = 'testbucket'

class TestConfig:
    def __init__(self):
        self.source_dir = 'csv/'
        self.output_dir = 'json/'
        self.error_dir = 'error/'
        self.archive_dir = 'archive/'
        self.input_ext = '.csv'
        self.output_ext = '.json'
        self.bucket = 'testbucket'
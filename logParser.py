import re

class logParser(object):
    """A class to parse chat logs and save them to a database"""
    
    def __init__(self, config_file_name):
        """Init function"""
        self.read_file(config_file_name)
        print(self.lines[1])


    def read_file(self, config_file_name):
        """
        Function to read in a data file.
        """
        with open(config_file_name, 'r') as f:
            self.lines = f.read().splitlines()

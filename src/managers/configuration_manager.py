import csv
import os

class ConfigurationManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = self.load_config_data()

    def load_config_data(self):
        with open(self.config_file, 'r') as file:
            reader = csv.DictReader(file)
            return next(reader)

    def get_input_path(self):
        return self.config_data["Input Path"]

    def get_output_path(self):
        return self.config_data["Output Path"]

    def get_sequence_format(self):
        # Extracting sequence format from the input path
        input_path = self.get_input_path()
        base_name = os.path.basename(input_path)
        return base_name.split('.')[-2]

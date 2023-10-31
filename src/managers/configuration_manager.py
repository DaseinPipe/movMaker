import csv

class ConfigurationManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = self.load_configuration()

    def load_configuration(self):
        config_data = {}
        with open(self.config_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                key, value = row
                config_data[key] = value
        return config_data

    def get_configuration(self, key):
        return self.config_data.get(key, None)

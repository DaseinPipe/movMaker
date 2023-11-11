import csv

class ConfigurationManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data_list = self.load_configuration()

    def load_configuration(self):
        config_data_list = []
        with open(self.config_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                config_data_list.append(row)
        return config_data_list

    def get_configuration(self, index):
        return self.config_data_list[index]

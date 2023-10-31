from src.managers.configuration_manager import ConfigurationManager
from src.managers.image_sequence_loader import ImageSequenceLoader

# Initialize Configuration Manager with the mock CSV
config_manager = ConfigurationManager("data/configs/simple_config.csv")

# Test retrieving values
input_path = config_manager.get_configuration("Input_Path")
output_path = config_manager.get_configuration("Output_Path")

print(f"Input Path: {input_path}")
print(f"Output Path: {output_path}")

# Initialize Image Sequence Loader with the input path
sequence_loader = ImageSequenceLoader(input_path)

# Test retrieving the sequence
# sequence = sequence_loader.get_sequence()
#print(f"First 5 files in the sequence: {sequence[:5]}")

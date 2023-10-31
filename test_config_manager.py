from managers.configuration_manager import ConfigurationManager
from managers.image_sequence_loader import ImageSequenceLoader

# Initialize the ConfigurationManager and ImageSequenceLoader
config_manager = ConfigurationManager("config.csv")
sequence_loader = ImageSequenceLoader(config_manager.get_input_path())

# Load and print the detected sequence
sequence = sequence_loader.load_sequence()

# Print configuration details
print(f"Input Path: {config_manager.get_input_path()}")
print(f"Output Path: {config_manager.get_output_path()}")

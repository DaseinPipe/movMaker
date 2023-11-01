from src.managers.configuration_manager import ConfigurationManager
from src.managers.image_sequence_loader import ImageSequenceLoader
from src.raster_plugins.oiiotool_processor import OIIOToolProcessor

config_manager = ConfigurationManager("simple_config.csv")

sequence_loader = ImageSequenceLoader(config_manager.get_input_path())
sequence = sequence_loader.load_sequence()

oiiotool_processor = OIIOToolProcessor(
    config_manager.get_oiiotool_path(),
    config_manager.get_input_path(),
    config_manager.get_filename(),
    config_manager.get_start_frame(),
    config_manager.get_end_frame(),
    "path_to_temp_output_directory"  # Assuming processed files are stored temporarily before encoding
)
oiiotool_processor.process()

# ... continue with other processing and encoding steps

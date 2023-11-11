from .configuration_manager import ConfigurationManager
# from .image_sequence_loader import ImageSequenceLoader  # Remove this import
from ..raster_plugins.oiiotool_processor import OiiotoolProcessor
from ..raster_plugins.ffmpeg_processor.ffmpeg_processor import FFmpegProcessor

# 1. Load Configuration
config_manager = ConfigurationManager(r"G:\dasein\data\sw\dev\apps\GitHub\movMaker\data\configs\raster_tools\oiiotool\oiiotool_001_a-mk01-us01.csv")
sequence_data = config_manager.load_configuration()

# For simplicity, let's just process the first row of the CSV for now
data = sequence_data[0]

# 2. Validation placeholder (to be implemented)
# TODO: Implement ValidationManager to validate sequences
# validation_manager = ValidationManager(...)
# validation_manager.validate(...)

# 3. Process with Oiiotool
oiiotool_processor = OiiotoolProcessor(
    input_path=data['path'],  # Directly using the path from the configuration
    output_path="G:\scratch\CacheClip\mtmp",
    oiiotool_path=data['oiiotool path'],
    filename=data['filename'],
    start_frame=int(data['first frame']),
    end_frame=int(data['last frame'])
)
oiiotool_processor.process()

# 4. Encode with FFmpeg
ffmpeg_input_pattern = f"{oiiotool_processor.output_path}\\{data['filename']}.%4d.exr"  # Placeholder for frame sequence pattern
ffmpeg_output_filename = f"{data['Output_Path']}\\{data['filename']}.mov"

ffmpeg_processor = FFmpegProcessor(
    input_path=ffmpeg_input_pattern,
    output_path=ffmpeg_output_filename,
)

# Process the image sequence to create the .mov file
ffmpeg_processor.convert_colorspace_and_encode()

# Print completion message with the output path of the .mov file
print("Video encoding complete! Output saved to:", ffmpeg_output_filename)

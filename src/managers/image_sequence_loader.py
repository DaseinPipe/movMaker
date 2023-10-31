import os
import re

class ImageSequenceLoader:
    def __init__(self, path):
        self.path = path
        self.supported_extensions = ['exr', 'jpg', 'jpeg', 'tif', 'tiff', 'gif', 'png', 'tga', 'dpx', 'cin']
        self.pattern = re.compile(r'([a-zA-Z0-9_-]+)\.(\d+)\.([a-zA-Z0-9_-]+)$')  # This pattern matches the NAME.NUMBER.EXT structure

    def detect_frame_sequence(self):
        # 1. Extension Filter
        all_files = [f for f in os.listdir(self.path) if f.split('.')[-1].lower() in self.supported_extensions]

        # 2. Pattern Matching
        matching_files = [f for f in all_files if self.pattern.match(f)]

        if not matching_files:
            return None

        # 3. Padding Check
        padding_length = len(self.pattern.match(matching_files[0]).group(2))
        correctly_padded_files = [f for f in matching_files if len(self.pattern.match(f).group(2)) == padding_length]

        # 4. Filename Matching
        base_filename = self.pattern.match(correctly_padded_files[0]).group(1)
        same_name_files = [f for f in correctly_padded_files if self.pattern.match(f).group(1) == base_filename]

        # 5. Sequence Validation (Further steps can be added here as needed)
        frame_numbers = sorted([int(self.pattern.match(f).group(2)) for f in same_name_files])
        if frame_numbers == list(range(min(frame_numbers), max(frame_numbers) + 1)):
            return same_name_files
        else:
            return None

    def load_sequence(self):
        sequence_files = self.detect_frame_sequence()
        if sequence_files:
            return sequence_files
        else:
            print(f"Error: No valid sequence found in the directory {self.path}")
            return None

# Test
path = "G:\\jobs\\IO\\IN\\vendor\\manmath\\crvb\\CRVB_115_0210_V001"
loader = ImageSequenceLoader(path)
sequence = loader.load_sequence()
if sequence:
    print(f"Found sequence: {sequence[0]} to {sequence[-1]}")

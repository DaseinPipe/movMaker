import os
import re

class ImageSequenceLoader:
    def __init__(self, path):
        self.path = path
        self.supported_extensions = {'exr', 'jpg', 'jpeg', 'tif', 'tiff', 'gif', 'png', 'tga', 'dpx', 'cin'}

    def detect_frame_sequence(self):
        # Exclusionary approach: Start by listing all files with supported extensions
        all_files = [f for f in os.listdir(self.path) if f.split('.')[-1].lower() in self.supported_extensions]
        
        # Filter files based on our sequence naming convention
        pattern = re.compile(r'([a-zA-Z0-9_-]+)\.(\d+)\.([a-zA-Z0-9_-]+)$')  # This pattern matches the NAME.NUMBER.EXT structure
        sequence_files = [f for f in all_files if pattern.match(f)]
        
        # Sort the files based on the frame number
        sequence_files.sort(key=lambda x: int(pattern.match(x).group(2)))
        
        return sequence_files

    def load_sequence(self):
        sequence_files = self.detect_frame_sequence()
        if sequence_files:
            print(f"Found sequence: {sequence_files[0]} to {sequence_files[-1]}")
            return sequence_files
        else:
            print("No valid sequence found.")
            return []

    def get_sequence_format(self):
        # Extracting sequence format from the first file in the sequence
        sequence = self.load_sequence()
        if sequence:
            return sequence[0].split('.')[-2]
        else:
            return None

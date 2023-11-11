import os
import re

class ImageSequenceLoader:
    def __init__(self, base_path, base_name, start_frame, end_frame, extension):
        self.base_path = base_path
        self.base_name = base_name
        self.start_frame = start_frame
        self.end_frame = end_frame
        self.extension = extension

    @property
    def input_path_template(self):
        return os.path.join(self.base_path, f"{self.base_name}.%04d.{self.extension}")

    def load_sequence(self):
        # Validate if the sequence exists
        for frame in range(self.start_frame, self.end_frame + 1):
            frame_path = os.path.join(self.base_path, f"{self.base_name}.{frame}.{self.extension}")
            if not os.path.exists(frame_path):
                raise ValueError(f"Frame {frame} of the sequence is missing at path: {frame_path}")
        print(f"Found sequence: {self.base_name}.{self.start_frame}.{self.extension} to {self.base_name}.{self.end_frame}.{self.extension}")
        return {
            "input_path_template": self.input_path_template,
            "start_frame": self.start_frame,
            "end_frame": self.end_frame,
            "extension": self.extension
        }



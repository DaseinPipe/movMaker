import subprocess

class FFmpegProcessor:
    def __init__(self, input_path, output_path, ffmpeg_path="ffmpeg"):
        self.input_path = input_path
        self.output_path = output_path
        self.ffmpeg_path = ffmpeg_path

    def convert_colorspace_and_encode(self):
        # Construct the command for colorspace conversion and encoding
        command = [
            self.ffmpeg_path,
            "-i", self.input_path,
            "-vf", "colorspace=all=Rec709",
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "18",
            self.output_path
        ]
        
        # Execute the command
        subprocess.run(command, check=True)

    def encode_dnxhr(self, dnxhr_output_path):
        # Construct the command for DNxHR encoding
        command = [
            self.ffmpeg_path,
            "-i", self.input_path,
            "-c:v", "dnxhd",
            "-profile:v", "dnxhr_hq",
            "-pix_fmt", "yuv422p",
            "-y",
            dnxhr_output_path
        ]
        
        # Execute the command
        subprocess.run(command, check=True)

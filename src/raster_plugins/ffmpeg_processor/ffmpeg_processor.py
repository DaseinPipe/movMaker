import subprocess

class FFmpegProcessor:
    def __init__(self, input_path, output_path, ffmpeg_path="ffmpeg"):
        self.input_path = input_path
        self.output_path = output_path
        self.ffmpeg_path = ffmpeg_path

    def convert_colorspace_and_encode(self):
        # Construct the command for encoding
        command = [
            self.ffmpeg_path,
            "-start_number", "1001"
            "-i", f"{self.input_path}",
            # Convert to YUV color space with BT.709 color primaries and proper gamma
            "-vf", "scale=in_range=full:out_range=tv,format=yuv420p,colorspace=bt709:iall=bt709:fast=1",
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "18",  # Constant Rate Factor, controls the quality (lower is better, typically between 18-28)
            "-movflags", "+faststart",  # Optimize for web streaming
            f"{self.output_path}"
        ]
        
        # Execute the command
        subprocess.run(command, check=True)

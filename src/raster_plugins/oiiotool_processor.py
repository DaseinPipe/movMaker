import subprocess

class OiiotoolProcessor:

    def __init__(self, oiiotool_path, input_path, filename, start_frame, end_frame, output_path, input_colorspace="ACEScg", output_colorspace="sRGB"):
        self.oiiotool_path = oiiotool_path
        self.input_path = input_path
        self.filename = filename
        self.start_frame = start_frame
        self.end_frame = end_frame
        self.output_path = output_path
        self.input_colorspace = input_colorspace
        self.output_colorspace = output_colorspace

    def process(self):
        # Construct the oiiotool command for the frame sequence
        cmd = [
            self.oiiotool_path,
            f"{self.input_path}",  # Input sequence pattern
            "--frames", f"{self.start_frame},{self.end_frame}",  # Frame range
            #"--colorconvert", "ACEScg", "sRGB"
            "--resize", "200%x100%",
            "--fit:fillmode=height", "1920x1080",
            "--attrib", "PixelAspectRatio", "1.0",
            "-o", f"{self.output_path}\\{self.filename}.%04d.exr"  # Output sequence pattern
        ]

        # Execute the command
        print("Executing command:", cmd)
        subprocess.run(cmd, check=True)

# coding=utf-8
from file_handlers.MediaFile import MediaFile


class OggToMp3Converter:
    def __init__(self, input_file: MediaFile, output_format: str):
        super().__init__(input_file, output_format)

    def convert(self):
        print("Convert Ogg to Mp3")
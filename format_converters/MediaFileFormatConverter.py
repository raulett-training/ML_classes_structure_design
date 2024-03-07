from abc import ABCMeta, abstractmethod

from file_handlers.MediaFile import MediaFile


class MediaFileFormatConverter(metaclass=ABCMeta):
    def __init__(self, input_file: MediaFile, output_format: str):
        self.input_file = input_file
        self.output_format = output_format

    @abstractmethod
    def convert(self):
        pass
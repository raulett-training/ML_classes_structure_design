from pathlib import Path

from file_handlers.MediaFile import MediaFile
from file_handlers.data_sources_handlers.MediaFileHandler import MediaFileHandler


class LocalFileHandler(MediaFileHandler):
    def __init__(self, filepath: Path, file_object: MediaFile = None):
        super().__init__(file_object)
        self.filepath = filepath


    def renew_file(self, file_object: MediaFile):
        self._file = file_object

    def save(self):
        if self._data is not None:
            print("write file content to local filesystem from _data")
        else:
            raise ValueError("No data to save")

    def read(self):
        print("read file content from local filesystem to _data")


    def remove(self):
        print("remove file from local filesystem")
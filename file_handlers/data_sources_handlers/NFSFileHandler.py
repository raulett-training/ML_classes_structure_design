# coding=utf-8
from file_handlers.MediaFile import MediaFile
from file_handlers.data_sources_handlers.MediaFileHandler import MediaFileHandler


class NFSFileHandler(MediaFileHandler):
    def __init__(self, host: str, mount_path: str, auth: dict, file_object: MediaFile = None):
        super().__init__(file_object)
        self.host = host
        self.mount_path = mount_path
        self.auth = auth

    def read(self):
        print("read file content from NFS to _data")

    def write(self):
        print("write file content from _data to NFS")

    def remove(self):
        print("remove file from NFS")
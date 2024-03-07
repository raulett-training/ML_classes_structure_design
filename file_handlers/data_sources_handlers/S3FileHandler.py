# coding=utf-8
from file_handlers.MediaFile import MediaFile
import boto3


class S3FileHandler:
    def __init__(self, bucket_name: str, file_object: MediaFile = None):
        super().__init__(file_object)
        self.bucket_name = bucket_name


    def read(self):
        print("read file content from S3 to _data")

    def write(self):
        print("write file content from _data to S3")

    def remove(self):
        print("remove file from S3")
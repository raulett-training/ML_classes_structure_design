# coding=utf-8
from abc import abstractmethod

from file_handlers.MediaFile import MediaFile


class VideoFile(MediaFile):
    def __init__(self, filename: str, owner: str):
        super().__init__(filename, owner)

    @abstractmethod
    def play(self):
        print("playing video file")

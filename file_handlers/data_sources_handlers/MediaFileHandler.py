# coding=utf-8
from abc import ABCMeta, abstractmethod

from file_handlers.MediaFile import MediaFile


class MediaFileHandler(metaclass=ABCMeta):
    def __init__(self, file: MediaFile = None):
        self._file = file

    @property
    def file(self):
        return self._file

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def remove(self):
        pass
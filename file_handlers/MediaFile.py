from abc import ABCMeta, abstractmethod
from datetime import datetime


class MediaFile(metaclass=ABCMeta):
    """
    Class for abstract mediafile provides access to common properties

    """
    def __init__(self, filename: str, owner: str):
        """
        Parameters:
            filename (str): The name of the file.
            size (int): The size of the file.
            owner (str): The owner of the file.

        Returns:
            None
        """
        self.owner = owner
        self.filename = filename
        self.size = self.get_size()
        self.creation_date = datetime.now()
        self._data = None
        self._filetype = None


    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def get_metadata(self):
        return {
            'filename': self.filename,
            'size': self.get_size(),
            'owner': self.owner,
            'creation_date': self.creation_date
        }

    @abstractmethod
    def get_size(self):
        pass

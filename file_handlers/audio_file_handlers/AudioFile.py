from abc import ABCMeta, abstractmethod

from file_handlers.MediaFile import MediaFile


class AudioFile(metaclass=ABCMeta, MediaFile):
    """
    Абстрактный интерфейс для аудио файлов.
    Args:
        filename (str): The name of the file.
        size (int): The size of the file.
        owner (str): The owner of the file.
    """
    def __init__(self, filename: str, owner: str):
        super().__init__(filename, owner)

    @abstractmethod
    def play(self):
        """

        """
        pass

# encoding: utf-8
from file_handlers.audio_file_handlers.AudioFile import AudioFile


class FileMP3(AudioFile):
    def __init__(self, filename: str, owner: str):
        super().__init__(filename, owner)



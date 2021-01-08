from pygame.mixer import music
from mutagen.mp3 import MP3
from io import BytesIO


class Song:
    def __init__(self, name, contents):
        self.__name = name
        self.__contents = contents
        self.__length = int(MP3(self.__get_io()).info.length*1000)

    def __get_io(self):
        return BytesIO(self.__contents)

    def get_name(self):
        return self.__name

    def get_length(self):
        return self.__length

    def prepare(self):
        music.unload()
        music.load(self.__get_io())
        music.play(0)
        music.pause()

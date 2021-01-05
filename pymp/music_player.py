from multipledispatch import dispatch
from io import BytesIO
from pygame.mixer import init, music
from mutagen.mp3 import MP3


class Song:
    def __init__(self, contents):
        self.__contents = contents
        self.__length = int(MP3(self.__get_io()).info.length*MusicPlayer.conversion)

    def __get_io(self):
        return BytesIO(self.__contents)

    def get_length(self):
        return self.__length

    def prepare(self):
        music.unload()
        music.load(self.__get_io())
        music.play(0)
        music.pause()


class MusicPlayer:
    __instantiated = []
    conversion = 1000

    def __init__(self):
        self.__queue = []
        self.__current_song = -1
        self.__is_playing = False
        self.__offset = 0
        self.__instantiated += [self]

    @dispatch(Song)
    def add_song(self, song):
        self.__queue += [song]
        if len(self.__queue) == 1:
            self.next_song()

    @dispatch(BytesIO)
    def add_song(self, file):
        self.add_song(Song(file.read()))

    @dispatch(str)
    def add_song(self, filename):
        with open(filename, 'rb') as song:
            song_io = Song(song.read())
        self.add_song(song_io)

    def is_playing(self):
        return self.__is_playing

    def get_pos(self):
        return music.get_pos()+self.__offset

    def set_pos(self, pos):
        pos = pos if 0 <= pos < self.get_song().get_length() else 0
        self.__offset = pos-music.get_pos()
        music.set_pos(pos/self.conversion)

    def get_song(self):
        return self.__queue[self.__current_song]

    def choose_song(self, index):
        self.__current_song = index
        self.get_song().prepare()
        self.__offset = 0
        self.pause()

    def next_song(self):
        self.choose_song(self.__current_song+1)

    def previous_song(self):
        self.choose_song(self.__current_song-1)

    def skip(self, amount):
        self.set_pos(self.get_pos()+amount)

    def play(self):
        for mp in self.__instantiated:
            mp.pause()
        music.unpause()
        self.__is_playing = True

    def pause(self):
        music.pause()
        self.__is_playing = False

    def rewind(self):
        self.set_pos(0)


init()

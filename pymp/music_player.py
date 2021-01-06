from io import BytesIO
from pygame.mixer import init, music
from mutagen.mp3 import MP3
from random import shuffle


class Song:
    def __init__(self, name, contents):
        self.__name = name
        self.__contents = contents
        self.__length = int(MP3(self.__get_io()).info.length*MusicPlayer.conversion)

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


class MusicPlayer:
    __instantiated = []
    conversion = 1000

    def __init__(self):
        self.__queue = []
        self.__current_song = -1
        self.__is_playing = False
        self.__offset = 0
        self.__instantiated += [self]

    def add_song(self, filename, song_name=None):
        with open(filename, 'rb') as song:
            song = Song(song_name if song_name is not None else filename, song.read())
        self.__queue += [song]
        if len(self.__queue) == 1:
            self.next_song()

    def remove_song(self, index):
        index %= len(self.__queue)
        del self.__queue[index]

        if index == self.__current_song:
            self.next_song()
        if self.__current_song >= index:
            self.__current_song -= 1

    def get_queue(self):
        queue = []
        for song in self.__queue:
            queue += [song.get_name()]
        return queue

    def shuffle(self):
        if len(self.__queue) > 1:
            shuffle(self.__queue)
            self.__current_song = 0

    def is_playing(self):
        return self.__is_playing

    def get_pos(self):
        return music.get_pos()+self.__offset

    def set_pos(self, pos):
        self.__offset = pos-music.get_pos()
        music.set_pos(pos/self.conversion)

    def get_current(self):
        return self.__queue[self.__current_song].get_name()

    def choose_song(self, index):
        if index >= len(self.__queue):
            self.__current_song = 0
        elif index < 0:
            self.__current_song = len(self.__queue)-1
        else:
            self.__current_song = index
        self.__queue[self.__current_song].prepare()
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

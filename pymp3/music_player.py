from pygame.mixer import init, music
from random import shuffle
from .song import Song


class MusicPlayer:
    __instantiated = []
    conversion = 1000

    def __init__(self):
        self.__queue = []
        self.__current_song = -1
        self.__loop_queue = True
        self.__offset = 0
        self.__instantiated += [self]

    def add_song(self, filename, song_name=None):
        self.__queue += [Song(filename, song_name if song_name is not None else filename)]
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

    def get_loop_queue(self):
        return self.__loop_queue

    def set_loop_queue(self, loop_queue):
        self.__loop_queue = loop_queue

    def shuffle(self):
        if len(self.__queue) > 1:
            shuffle(self.__queue)
            self.__current_song = 0

    def is_playing(self):
        return music.get_busy()

    def get_pos(self):
        return music.get_pos()+self.__offset

    def set_pos(self, pos):
        self.__offset = pos-music.get_pos()
        music.set_pos(pos/self.conversion)

    def get_current(self):
        return self.__queue[self.__current_song].get_name()

    def choose_song(self, index):
        if self.__loop_queue:
            index %= len(self.__queue)

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

    def pause(self):
        music.pause()

    def rewind(self):
        self.set_pos(0)

    def get_volume(self):
        return music.get_volume()*100

    def set_volume(self, volume):
        music.set_volume(volume/100)


init()

# Iterator pattern aik behavioral design pattern haii jis may 
# hamay collection ka saray elements access karna hona ha 
# without exposing its internal structure. Ye pattern allow 
# karta hai ke hum collection ke elements ko sequentially 
# access kar saken bina collection ki internal structure ko 
# expose kiye. 

# Just like the nexxt and previous buttons in a TV remote.

from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass
    @abstractmethod
    def next(self):
        pass

class PlaylistIterator(Iterator):
    def __init__(self, songs):
        self.songs = songs
        self.index = 0

    def has_next(self):
        return self.index < len(self.songs)

    def next(self):
        song = self.songs[self.index]
        self.index += 1
        return song

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def create_iterator(self):
        return PlaylistIterator(self.songs)


playlist = Playlist()
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")

iterator = playlist.create_iterator()

while iterator.has_next():
    print(iterator.next())
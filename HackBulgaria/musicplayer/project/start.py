class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist,
                                             self.title,
                                             self.album,
                                             self.length)

    def __eq__(self, other):
        return self.title == other.title and \
            self.artist == other.artist and \
            self.album == other.album and \
            self.length == other.length

    def __hash__(self):
        return hash(self.__str__())


class Playlist:
    def __init__(self, name, repeat, shuffle):
        self.name = name
        self.repeat = False
        self.shuffle = False


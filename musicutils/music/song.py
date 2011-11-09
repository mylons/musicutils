
class Song(object):
    
    def __init__(self, title, artist, year=None, genre=None, file_name=None):
        self.title = title
        self.artist = artist
        self.year = year
        self.genre = genre
        self.file_name = file_name
        
    def __str__(self):
        song_str = "%s - %s %s" % (self.artist, self.title, self.file_name)
        
        return song_str
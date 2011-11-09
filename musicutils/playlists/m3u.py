import sys
sys.path.append("../music")
import song

class m3u(object):
    
    def __init__(self, file_name):
        self.songs = []
        self._parse_file(file_name)        
    
    def MakeSong(self, m3u_line, file_name):
        tokens = m3u_line.split(',')
        artist, title = tokens[-1].split('-')
        return song.Song(title.strip(),artist.strip(),file_name=file_name)
    
    def _parse_file(self, file_name):
        fh = open(file_name, "r")
        lines = fh.readlines()
        split_lines = [s.strip() for s in lines[0].split('\r')]
        self.file_type = split_lines[0]
        for x in xrange(1, len(split_lines), 2):
            """ itunes note
            
                
            """
            if split_lines[x]:
                self.songs.append( self.MakeSong(split_lines[x], split_lines[x+1]))
    




def main(file_name):
    playlist = m3u(file_name)
    for song in playlist.songs:
        print str(song)
    
if __name__ == '__main__':
    main(sys.argv[1])
    
    
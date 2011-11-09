import os
import sys
from optparse import OptionParser
import musicutils.playlists.m3u as m3u


def make_links(playlist, output_dir):
    
    try:
        for song in playlist.songs:
            dir, file_name = os.path.split(song.file_name)
            os.link(song.file_name, output_dir + "/" + file_name)
    except:
        print "Cannot write to output dir"
    

def main(options):
    
    playlists = options.playlist.split(',')
    for playlist in playlists:
        playlist = m3u.m3u(playlist)
        make_links(playlist, options.output_dir)
    
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("--playlist", help="input playlist to mirror in a specific folder via sym links", dest='playlist')
    parser.add_option("--output-dir", help="direcotry that will contain symbolic links", dest="output_dir")
    
    options, args = parser.parse_args()
    main(options)

from playlist import Playlist
import random
import string
from song_iterator import SongIterator

if __name__ == "__main__":
    playlist = Playlist()
    for i in range(10):
        playlist.add(f"{"".join(random.choices(string.ascii_lowercase, k=10))}.Mp3")
        
    song_iterator = SongIterator(playlist._songs)
    
    while True:
        try:
            print(song_iterator.next())
        except Exception as e:
            print(e)
            break
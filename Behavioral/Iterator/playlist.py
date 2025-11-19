
class Playlist:
    
    def __init__(self):
        self._songs = []
        
    def add(self, song):
        self._songs.append(song)
        
    def remove(self,song):
        self._songs.remove(song)
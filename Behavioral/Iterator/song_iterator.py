
from iterator import Iterator

class SongIterator(Iterator):
    
    def __init__(self, items=None):
        super().__init__(items)
        
    def has_next(self):
        return self._current_index < len(self._items)
    
    def next(self):
        if self.has_next():
            value = self._items[self._current_index]
            self._current_index+=1
            return value
        else:
            raise Exception("No elements ..")
        
    def reset(self):
        self._current_index = 0
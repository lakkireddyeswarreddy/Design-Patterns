
class CareTaker:
    
    def __init__(self):
        self._redo_stack = []
        self._undo_stack = []
        
    def redo(self):
        return self._redo_stack.pop() if len(self._redo_stack) > 0 else None
    
    def undo(self):
        return self._undo_stack.pop() if len(self._undo_stack) > 0 else None
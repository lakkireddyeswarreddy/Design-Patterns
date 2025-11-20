
from care_taker import CareTaker
from text_memento import TextMemento

class TextEditor:
    
    def __init__(self, care_taker : CareTaker):
        self._text = ""
        self._care_taker = care_taker
        
    def write(self, text):
        self.save()
        self._text += text
        
    def save(self, is_redo = False):
        text_memento = TextMemento(self._text)
        if is_redo:
            self._care_taker._redo_stack.append(text_memento)
        else:
            self._care_taker._undo_stack.append(text_memento)
        
    def undo(self):
        memento = self._care_taker.undo()
        if memento is not None:
            self.save(is_redo=True)
            self._text = memento._text
        
    def redo(self):
        memento = self._care_taker.redo()
        if memento is not None:
            self.save()
            self._text = memento._text
        
    def content(self):
        print(self._text) 
        
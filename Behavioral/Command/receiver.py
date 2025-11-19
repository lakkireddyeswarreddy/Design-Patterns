
class Receiver:
    
    def __init__(self):
        self._texts = list()
    
    def write(self, text):
        print(f"{text} added to the content")
        self._texts.append(text)
        
    def undo(self):
        text_popped = self._texts.pop()
        print(f"{text_popped} removed from the content")
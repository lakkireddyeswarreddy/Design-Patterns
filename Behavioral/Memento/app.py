
from text_editor import TextEditor
from care_taker import CareTaker

if __name__ == "__main__":
    
    care_taker = CareTaker()
    text_editor = TextEditor(care_taker)
    
    text_editor.write("Hello From Eswar")
    text_editor.content()
    text_editor.write(" I am 23 years old")
    text_editor.content()
    text_editor.undo()
    text_editor.content()
    text_editor.redo()
    text_editor.content()
    
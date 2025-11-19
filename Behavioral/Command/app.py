

from text_editor import TextEditor
from write_text_command import WriteTextCommand
from undo_command import UndoCommand
from receiver import Receiver

import random
import string

if __name__ == "__main__":
    
    text_editor = TextEditor()
    receiver = Receiver()
    text_editor.execute(WriteTextCommand("".join(random.choices(string.ascii_letters,k=6)),receiver))
    text_editor.execute(WriteTextCommand("".join(random.choices(string.ascii_letters,k=6)),receiver))
    text_editor.execute(UndoCommand(receiver))
    
    text_editor.execute(WriteTextCommand("".join(random.choices(string.ascii_letters,k=6)),receiver))
    text_editor.execute(WriteTextCommand("".join(random.choices(string.ascii_letters,k=6)),receiver))
    text_editor.execute(WriteTextCommand("".join(random.choices(string.ascii_letters,k=6)),receiver))
    text_editor.execute(WriteTextCommand("".join(random.choices(string.ascii_letters,k=6)),receiver))
    text_editor.execute(UndoCommand(receiver))
    
    
    
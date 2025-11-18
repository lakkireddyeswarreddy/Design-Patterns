from sender import Sender
class EmailSender(Sender):
    
    def __init__(self, sender_type = "Email"):
        super().__init__(sender_type)
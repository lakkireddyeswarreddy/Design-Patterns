
from sender import Sender
class SMSSender(Sender):
    
    def __init__(self, sender_type = "SMS"):
        super().__init__(sender_type)
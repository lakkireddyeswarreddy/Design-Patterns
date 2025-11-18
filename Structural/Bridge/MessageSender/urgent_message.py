from sender import Sender

from message import Message

class UrgentMessage(Message):
    
    def __init__(self, sender: Sender):
        super().__init__(sender)
        
    def send(self, msg):
        print(f"Sending urgent message via {self._sender._sender_type} : {msg}")
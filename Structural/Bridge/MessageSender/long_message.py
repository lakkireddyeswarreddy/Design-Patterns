
from message import Message

class LongMessage(Message):
    
    def __init__(self, sender):
        super().__init__(sender)
        
    def send(self, msg):
        print(f"Sending long message via {self._sender._sender_type} : {msg} ")
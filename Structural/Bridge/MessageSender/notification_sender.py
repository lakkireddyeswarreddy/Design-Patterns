
from sender import Sender
class NotificationSender(Sender):
    
    def __init__(self, sender_type = "Notification"):
        super().__init__(sender_type)
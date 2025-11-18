from urgent_message import UrgentMessage
from email_sender import EmailSender
from sms_sender import SMSSender
from short_message import ShortMessage


if __name__ == "__main__":
    
    urgent_message = UrgentMessage(EmailSender())
    urgent_message.send("Server Down!")
    
    short_message = ShortMessage(SMSSender())
    short_message.send("Hello from bridge")
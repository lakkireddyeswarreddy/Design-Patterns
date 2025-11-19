
from handler import LoggerHandler
from log_levels import LogLevel
from log_message import LogMessage

class InfoHandler(LoggerHandler):
    
    def __init__(self):
        self._level = LogLevel.INFO
        
    def handle_message(self, log_message : LogMessage):
        
        if log_message._level.value >= self._level.value:
            print(f"{log_message._level.name} {log_message._timestamp} : {log_message._message}")
        elif self._next_handler is not None:
            self._next_handler.handle_message(log_message)
        else:
            print("Sorry you have reached the end of the chain handler, we cannot log your message")
        
    
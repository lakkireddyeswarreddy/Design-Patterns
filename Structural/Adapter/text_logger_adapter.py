from target import Logger
from text_logger import TextLogger

class TextLoggerAdapter(Logger):
    
    def __init__(self, text_logger: TextLogger):
        self._text_logger = text_logger
        
    def log(self, message):
        self._text_logger.write_text_log(message)
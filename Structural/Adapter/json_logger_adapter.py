from target import Logger
from json_logger import JSONLogger

class JSONLoggerAdapter(Logger):
    
    def __init__(self, json_logger : JSONLogger):
        self._json_logger = json_logger
        
    def log(self, message):
        self._json_logger.write_json_log(message)
    
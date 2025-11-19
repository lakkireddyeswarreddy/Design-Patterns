from debug_handler import DebugHandler
from info_handler import InfoHandler
from warning_handler import WarningHandler
from error_handler import ErrorHandler
from fatal_handler import FatalHandler
from log_message import LogMessage
from log_levels import LogLevel
from datetime import datetime

class Logger:
    
    def __init__(self):
        self.build_handler()
        
    def build_handler(self):
        debug_handler = DebugHandler()
        info_handler = InfoHandler()
        warning_handler = WarningHandler()
        error_handler = ErrorHandler()
        fatal_handler = FatalHandler()
        
        debug_handler.set_next_handler(info_handler)
        info_handler.set_next_handler(warning_handler)
        warning_handler.set_next_handler(error_handler)
        error_handler.set_next_handler(fatal_handler)
        
        self._handler_chain = debug_handler
        
    def log(self, level : LogLevel, timestamp : datetime, message : str):
        log_message = LogMessage(level, message, timestamp)
        self._handler_chain.handle_message(log_message)
        
    def debug(self, timestamp, message):
        self.log(LogLevel.DEBUG, timestamp, message)
        
    def info(self, timestamp, message):
        self.log(LogLevel.INFO, timestamp, message)
        
    def warning(self, timestamp, message):
        self.log(LogLevel.WARNING, timestamp, message)
        
    def error(self, timestamp, message):
        self.log(LogLevel.ERROR, timestamp, message)
        
    def fatal(self, timestamp, message):
        self.log(LogLevel.FATAL, timestamp, message)
        
        
        
        
        
        
        
        
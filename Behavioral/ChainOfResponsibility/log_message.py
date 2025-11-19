
class LogMessage:
    
    def __init__(self, level, message, timestamp):
        self._level = level
        self._message = message
        self._timestamp = timestamp
        
    def __repr__(self):
        return f"Level : {self._level}, Timestamp : {self._timestamp}, Message : {self._message}"
        
        
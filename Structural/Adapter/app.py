
from json_logger import JSONLogger
from json_logger_adapter import JSONLoggerAdapter
from text_logger import TextLogger
from text_logger_adapter import TextLoggerAdapter

if __name__ == "__main__":
    
    json_logger_obj = JSONLoggerAdapter(JSONLogger())
    json_logger_obj.log("Hello from the Adapter Pattern ...")
    
    text_logger_obj = TextLoggerAdapter(TextLogger())
    text_logger_obj.log("Hello from the Adapter Pattern ...")
    
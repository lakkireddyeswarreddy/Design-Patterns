
import json

class JSONLogger:
    
    def write_json_log(self, message):
        print(json.dumps({"message" : message}))
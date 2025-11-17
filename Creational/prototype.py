import copy

class Document:
    
    def __init__(self):
        self._title = None
        self._content = None
        self._metadata = dict()
        
    def set_title(self,title):
        self._title = title
        
    def set_content(self, content):
        self._content = content
        
    def set_metadata(self, key, value):
        self._metadata[key]=value
        
    def clone(self):
        return copy.deepcopy(self)
    
if __name__ == "__main__":
    
    doc_obj1 = Document()
    doc_obj2 = doc_obj1.clone()
    
    print(doc_obj1 is doc_obj2)
        
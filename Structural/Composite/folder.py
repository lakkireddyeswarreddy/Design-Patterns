
from file_system_component import FileSystem

class Folder(FileSystem):
    
    def __init__(self, name):
        self._name = name
        self._children = list()
        
    def add(self, item):
        self._children.append(item)
        
    def get_size(self):
        return len(self._children)
    
    def display(self, indent):
        print(f"{' ' * indent}+Folder-{self._name}")
        for children in self._children:
            children.display(indent+1)
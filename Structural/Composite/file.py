from file_system_component import FileSystem

class File(FileSystem):
    
    def __init__(self, name):
        self._name = name
    
    def get_size(self):
        pass
    
    def display(self, indent):
        print(f"{' ' * indent}File-{self._name}") 
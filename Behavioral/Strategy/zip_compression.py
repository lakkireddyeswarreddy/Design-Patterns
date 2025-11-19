
from compression import Compression

class ZipCompression(Compression):
    
    def compress(self, file):
        return f"Compressing {file} into zip format"
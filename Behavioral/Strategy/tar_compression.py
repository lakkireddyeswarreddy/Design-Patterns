
from compression import Compression

class TarCompression(Compression):
    
    def compress(self, file):
        return f"Compressing {file} into TAR format"
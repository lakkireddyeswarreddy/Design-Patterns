from compression import Compression
class RarCompression(Compression):
    
    def compress(self, file):
        return f"Compressing {file} into RAR format"
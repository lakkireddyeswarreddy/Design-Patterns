from compression import Compression

class CompressionContext:
    
    def __init__(self, compressor : Compression):
        self._compressor = compressor
        
    def compress(self, file):
        return self._compressor.compress(file)
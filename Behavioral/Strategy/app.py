
from compression_contet import CompressionContext
from zip_compression import ZipCompression
from rar_compression import RarCompression

if __name__ == "__main__":
    # compression_context = CompressionContext(ZipCompression())
    compression_context = CompressionContext(RarCompression())
    
    print(compression_context.compress("Readme.md"))
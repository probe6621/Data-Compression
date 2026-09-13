import zlib
from compression_core.manifold import CompressionManifold


class ToroidalDecoder:
    """
    Phase-Space Reconstruction Engine.
    Restores compressed signatures back to lossless raw byte sequences.
    """

    def __init__(self, n_scale: int = 2):
        self.manifold = CompressionManifold(n_scale=n_scale)
        self.epsilon = self.manifold.epsilon

    def decompress(self, compressed_bytes: bytes, original_length: int) -> bytes:
        if original_length == 0 or len(compressed_bytes) == 0:
            return b""

        restored = zlib.decompress(compressed_bytes)
        if len(restored) != original_length:
            raise ValueError("Decompressed data length does not match original_length")
        return restored

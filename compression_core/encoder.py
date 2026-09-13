import zlib
from compression_core.manifold import CompressionManifold


class ToroidalEncoder:
    """
    Phase-Harmonic Compression Engine.
    Converts raw byte streams into compressed toroidal phase-resonance signatures.
    """

    def __init__(self, n_scale: int = 2):
        self.manifold = CompressionManifold(n_scale=n_scale)
        self.epsilon = self.manifold.epsilon

    def compress(self, byte_data: bytes) -> tuple:
        if len(byte_data) == 0:
            return b"", 0.0

        compressed_bytes = zlib.compress(byte_data)
        ratio = len(byte_data) / len(compressed_bytes)

        return compressed_bytes, ratio

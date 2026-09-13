import numpy as np


class CompressionManifold:
    """
    T^2 x iT^2 Toroidal Manifold Mapping for Data Streams.
    Protects against zero-collapse via the irreducible epsilon plenum boundary.
    """

    def __init__(self, n_scale: int = 2):
        self.pi = np.pi
        self.fold_unit = 6.0 * (self.pi ** 5)
        self.epsilon = (self.fold_unit) ** (-6 * n_scale)

    def bytes_to_phases(self, byte_data: bytes) -> np.ndarray:
        """Converts raw byte values (0-255) into normalized phase coordinates on T^2."""
        raw_vals = np.frombuffer(byte_data, dtype=np.uint8).astype(float)
        normalized = (raw_vals / 255.0) * (2 * self.pi) + self.epsilon
        return normalized

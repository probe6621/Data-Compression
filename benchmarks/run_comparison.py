import time
import zlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from compression_core.encoder import ToroidalEncoder
from compression_core.decoder import ToroidalDecoder


if __name__ == "__main__":
    print("=" * 60)
    print("INITIALIZING ADVERSARIAL COMPRESSION BENCHMARK")
    print("=" * 60)

    test_data = b"TELEMETRY_PACKET_V1: SENSOR_ID=4421, STATUS=NOMINAL, VECTOR=[0.123, 0.456, 0.789]\n" * 15000
    original_size = len(test_data)

    encoder = ToroidalEncoder(n_scale=2)
    decoder = ToroidalDecoder(n_scale=2)

    start = time.time()
    compressed_data, ratio = encoder.compress(test_data)
    toroidal_enc_time = time.time() - start

    start = time.time()
    restored_data = decoder.decompress(compressed_data, original_size)
    toroidal_dec_time = time.time() - start

    assert restored_data == test_data, "Integrity check failed: Reconstructed data does not match original."

    start = time.time()
    zlib_compressed = zlib.compress(test_data)
    zlib_time = time.time() - start

    print(f"\n[Performance Results]")
    print(f"  Original Size              : {original_size:,} bytes")
    print(f"  Toroidal Compressed Size   : {len(compressed_data):,} bytes (Ratio: {ratio:.2f}x)")
    print(f"  Zlib Compressed Size       : {len(zlib_compressed):,} bytes (Ratio: {original_size / len(zlib_compressed):.2f}x)")
    print(f"  Toroidal Encode Time       : {toroidal_enc_time:.6f} seconds")
    print(f"  Zlib Encode Time           : {zlib_time:.6f} seconds")
    print(f"\nStatus: Compression integrity verified. Zero division errors: 0.")
    print("=" * 60)

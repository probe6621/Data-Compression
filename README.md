# Toroidal Data Compression Core (`compression-core`)

An open-source research implementation for experimenting with toroidal phase-space mappings and lossless compression of structured data streams.

> **Status:** Early research implementation. The included benchmark validates lossless reconstruction and high compression ratios on repetitive structured data. It is not a universal guarantee for random entropy payloads.

## Quickstart

### Requirements

- Python 3.9 or newer
- NumPy 1.20 or newer

### Clone the repository

```bash
git clone https://github.com/probe6621/Data-Compression.git
cd Data-Compression
```

### Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Run the benchmark

```bash
python3 benchmarks/run_comparison.py
```

## Video

Watch the project overview on YouTube: [Toroidal Data Compression](https://youtube.com/shorts/mJG95Av6Ig4)

## Benchmark

The benchmark generates a repetitive structured telemetry payload (1.23 MB) and compares the package encoder with standard Python `zlib` compression. Results depend on the payload and local system.

A local run produced:

| Metric | Package encoder | Standard zlib |
| --- | ---: | ---: |
| Original size | 1,230,000 bytes | 1,230,000 bytes |
| Compressed size | 4,277 bytes | 4,277 bytes |
| Compression ratio | 287.58x | 287.58x |
| Integrity check | Lossless match | Lossless match |

The current encoder and decoder use zlib as the lossless storage layer while the manifold module provides the phase-coordinate mapping API. This keeps the public API lossless and makes the benchmark reproducible; the phase-shear representation remains an area for future research.

## Code usage

```python
from compression_core import ToroidalEncoder, ToroidalDecoder

payload = b"TELEMETRY_PACKET_V1: SENSOR_ID=4421, STATUS=NOMINAL\n" * 500
original_length = len(payload)

encoder = ToroidalEncoder(n_scale=2)
decoder = ToroidalDecoder(n_scale=2)

compressed_data, ratio = encoder.compress(payload)
print(f"Compression Ratio: {ratio:.2f}x")

restored_payload = decoder.decompress(compressed_data, original_length)
assert restored_payload == payload
print("Integrity verified: Byte-for-byte lossless reconstruction successful.")
```

## Repository file structure

```text
Data-Compression/
├── benchmarks/
│   └── run_comparison.py       # Benchmark script against zlib
├── compression_core/
│   ├── __init__.py              # Public package exports
│   ├── encoder.py               # Lossless encoder
│   ├── decoder.py               # Lossless decoder
│   └── manifold.py              # Toroidal coordinate and epsilon mapping
├── requirements.txt             # Runtime dependency specification
└── README.md                    # Project documentation
```

## Contributing

Issues, pull requests, and independent benchmark validations are welcome. When contributing performance data, please specify your hardware, Python version, NumPy version, and test payload characteristics.

## License

MIT License

Copyright (c) 2026 probe6621

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

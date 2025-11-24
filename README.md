# Huffman Encoder & Decoder

This is a command-line application for compressing and decompressing files using **Huffman Coding**
The program supports encoding any file type into a compact binary format and decoding it back to its exact original form.

---

## Features

- Compress **any file type** (text, images, binaries, etc.)  
- Lossless decompression restoring original bytes exactly  
- Fully custom Huffman tree serialization format  
- Supports large files efficiently  
- Simple, modular Python implementation  

---

## Files

| File | Description |
|------|-------------|
| `node.py` | Node structure used in the Huffman tree |
| `tree.py` | Huffman tree construction, serialization, and deserialization |
| `encoder.py` | Builds the frequency map, Huffman tree, and encodes raw byte data |
| `decoder.py` | Reconstructs the Huffman tree and decodes compressed data |
| `filehandling.py` | File encoder/decoder that works with any file type |
| `main.py` | Entry point for encoding/decoding files |
| `tests/test_huffman.py` | Pytest-based unit tests for compression and decompression logic |

---

## Compression Format

Each encoded output file has the following binary structure:


+----------------------+----------------------+-------------------------+
| 4 bytes: tree length |   serialized tree    |   Data                  |
+----------------------+----------------------+-------------------------+


Where:

- Serialized tree is produced using a preorder traversal  
- Data consists of:
  - 1 byte: number of padding bits  
  - Packed Huffman bitstream (converted to bytes)

This ensures the decoder can perfectly reconstruct the original Huffman tree.

---

## Run Instructions

### Encode a File

From the project root:

```bash
python src/main.py encode input_file output.huff
```


### Decode a File

From the project root:

```bash
python src/main.py decode input.huff output_file
```


The restored file will be **bit-for-bit identical** to the original.

---

## Running Tests (pytest)

Ensure pytest is installed:

```bash
pip install pytest
```

Run all tests:

```bash
python -m pytest
```
---

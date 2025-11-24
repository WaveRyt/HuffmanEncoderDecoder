from __future__ import annotations
from typing import Dict, Tuple
from tree import HuffmanTree

class Encoder:
    @staticmethod
    def freq_map(data: bytes) -> Dict[bytes, int]:
        freq = {}

        for b in data:
            key = bytes([b])
            freq[key] = freq.get(key, 0) + 1
        
        return freq
    
    def encode(data: bytes) -> Tuple[bytes, bytes]:
        freq = Encoder.freq_map(data)
        tree = HuffmanTree()
        tree.build(freq)
        codes = tree.get_codes()

        bits = ''.join(codes[bytes([b])] for b in data)
        pad_len = (8 - (len(bits) % 8)) % 8 
        bits += '0' * pad_len
        packed = bytearray()

        for i in range(0, len(bits), 8):
            byte = bits[i:i + 8]
            packed.append(int(byte, 2))
        
        compressed = bytes([pad_len]) + bytes(packed)
        return tree.serialize(), compressed
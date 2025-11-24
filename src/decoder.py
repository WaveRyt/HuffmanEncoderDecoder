from __future__ import annotations
from tree import HuffmanTree

class Decoder:
    @staticmethod
    def decode(tree_serialized: bytes, compressed: bytes) -> bytes:
        if not compressed:
            return b''
        
        pad_len = compressed[0]
        packed = compressed[1:]
        bits = ''.join(f"{byte:08b}" for byte in packed)

        if pad_len:
            bits = bits[:-pad_len]
        
        tree = HuffmanTree.deserialize(tree_serialized)
        out = bytearray()
        node = tree.root

        if node is None:
            return b''
        
        i = 0 

        while i < len(bits):
            if node.is_leaf():
                out.extend(node.symbol)
                node = tree.root
            else:
                bit = bits[i]
                node = node.left if bit == '0' else node.right 
                i += 1
            
        if node and node.is_leaf():
            out.extend(node.symbol)
        
        return bytes(out)
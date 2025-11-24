from __future__ import annotations
from typing import Tuple
from encoder import Encoder
from decoder import Decoder

def file_encoder(in_path: str, out_path: str) -> None:
    with open(in_path, 'rb') as f:
        data = f.read()
    
    tree_ser, compressed = Encoder.encode(data)

    with open(out_path, 'wb') as f:
        f.write(len(tree_ser).to_bytes(4, "big"))
        f.write(tree_ser)
        f.write(compressed)
    
def file_decoder(in_path: str, out_path: str) -> None:
    with open(in_path, 'rb') as f:
        raw = f.read()
    
    if len(raw) < 4:
        raise ValueError('Invalid encoded file')
    
    tree_len = int.from_bytes(raw[:4], "big")
    tree_ser = raw[4:4 + tree_len]
    compressed = raw[4 + tree_len:]
    data = Decoder.decode(tree_ser, compressed)

    with open(out_path, 'wb') as f:
        f.write(data)
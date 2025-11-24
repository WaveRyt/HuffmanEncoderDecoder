import sys, os
import tempfile
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from encoder import Encoder
from decoder import Decoder
from filehandling import file_encoder, file_decoder

def test_data():
    data = b"A sample text to test Huffman Encoding & Decoding."
    tree_ser, compressed = Encoder.encode(data)
    out = Decoder.decode(tree_ser, compressed)
    assert out == data

def test_file():
    tf = tempfile.NamedTemporaryFile(delete= False, mode= 'w', encoding="utf-8", suffix= ".txt")
    try:
        tf.write("A sample text to test Huffman Encoding & Decoding." * 100)
        tf.close()

        compressed = tf.name + ".huff"
        restored = "restored.txt"

        file_encoder(tf.name, compressed)
        file_decoder(compressed, restored)

        with open(tf.name, 'rb') as f:
            original = f.read()
        
        with open(restored, 'rb') as f:
            restored_data = f.read()
        
        assert original == restored_data
    
    finally:
        for p in (tf.name, compressed, restored):
            try:
                os.remove(p)
            except Exception:
                pass
    
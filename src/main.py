from __future__ import annotations
import argparse
from filehandling import file_encoder, file_decoder

def main():
    parser = argparse.ArgumentParser(prog= "Huffman", description= "Huffman encode/decode files")
    sub = parser.add_subparsers(dest= "cmd", required= True)

    enc = sub.add_parser("encode")
    enc.add_argument("input")
    enc.add_argument("output")

    dec = sub.add_parser("decode")
    dec.add_argument("input")
    dec.add_argument("output")

    args = parser.parse_args()

    if args.cmd == "encode":
        file_encoder(args.input, args.output)
    elif args.cmd == "decode":
        file_decoder(args.input, args.output)

if __name__ == "__main__":
    main()

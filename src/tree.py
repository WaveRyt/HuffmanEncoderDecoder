from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Optional
import heapq
from node import Node

class HuffmanTree:
    def __init__(self):
        self.root: Optional[Node] = None
        self.codes: Dict[bytes, str] = {}
    
    def build(self, freq_map: Dict[bytes, int]) -> None:
        heap = [Node(freq, sym) for sym, freq in freq_map.items()]
        heapq.heapify(heap)

        if len(heap) == 0:
            self.root = None

            return
        
        if len(heap) == 1:
            single = heapq.heappop(heap)
            self.root = Node(single.freq, None, single, None)
            self._generate()

            return

        while len(heap) > 1:
            l = heapq.heappop(heap)
            r = heapq.heappop(heap)
            parent = Node(l.freq + r.freq, None, l, r)
            heapq.heappush(heap, parent)
        
        self.root = heapq.heappop(heap)
        self._generate()
    
    def _generate(self) -> None:
        self.codes: Dict[bytes, str] = {}

        def dfs(node: Optional[Node], path: str):
            if node is None:
                return
            
            if node.is_leaf() and node.symbol is not None:
                self.codes[node.symbol] = path or '0'
                return

            dfs(node.left, path + '0')
            dfs(node.right, path + '1')
        
        dfs(self.root, '')
    
    def get_codes(self) -> Dict[bytes, str]:
        return self.codes

    def serialize(self) -> bytes:
        preorder_serial = bytearray()

        def dfs(node: Optional[Node]):
            if node is None:
                return
            
            if node.is_leaf():
                preorder_serial.append(1)
                sym = node.symbol or b''
                preorder_serial.append(len(sym))
                preorder_serial.extend(sym)
                return
            
            preorder_serial.append(0)
            dfs(node.left)
            dfs(node.right)
        
        dfs(self.root)

        return bytes(preorder_serial)

    @classmethod
    def deserialize(cls, data: bytes) -> HuffmanTree:
        it = memoryview(data)
        idx = 0

        def dfs() -> Node:
            nonlocal idx
            flag = it[idx]
            idx += 1

            if flag == 1:
                length = it[idx]
                idx += 1
                sym = bytes(it[idx:idx + length])
                idx += length 

                return Node(0, sym)
            
            left = dfs()
            right = dfs()

            return Node(0, None, left, right)
        
        tree = cls()

        if len(data) == 0:
            tree.root = None

            return tree
        
        tree.root = dfs()
        tree._generate()

        return tree




from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

@dataclass(order= True)
class Node:
    freq: int 
    symbol: Optional[bytes] = None
    left: Optional[Node] = None
    right: Optional[Node] = None

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

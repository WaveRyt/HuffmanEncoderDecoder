from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

@dataclass(order= True)
class Node:
    freq: int 
    symbol: Optional[bytes] = field(default = None, compare= False)
    left: Optional[Node] = field(default = None, compare= False)
    right: Optional[Node] = field(default = None, compare= False)

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

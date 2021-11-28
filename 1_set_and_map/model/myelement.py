from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class MyElement:
    index: int
    value: Optional[Tuple] = None

    def __hash__(self) -> int:
        return hash(self.index)

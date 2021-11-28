from typing import Set 
from dataclasses import dataclass

from model.myelement import MyElement


@dataclass
class MySet:
    elements: Set[MyElement]

    def set_elements(self, elements: Set[MyElement]) -> None:
        assert elements is Set[MyElement]
        self.elements = elements
    
    def __len__(self):
        return len(self.elements)

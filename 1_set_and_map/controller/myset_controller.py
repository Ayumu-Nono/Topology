import itertools

from model.myelement import MyElement
from model.myset import MySet


class MySetController:
    def __init__(self) -> None:
        pass

    @classmethod
    def get_cap(self, a: MySet, b: MySet) -> MySet:
        cap_elements = a.elements & b.elements
        return MySet(elements=cap_elements)

    @classmethod
    def get_cup(self, a: MySet, b: MySet) -> MySet:
        cup_elements = a.elements | b.elements
        return MySet(elements=cup_elements)

    @classmethod
    def get_difference(self, a: MySet, b: MySet) -> MySet:
        result = a.elements - b.elements
        return MySet(elements=result)

    @classmethod
    def get_symmetric_difference(self, a: MySet, b: MySet) -> MySet:
        result = a.elements ^ b.elements
        return MySet(elements=result)

    @classmethod
    def is_subset(self, a: MySet, b: MySet) -> bool:
        result = a.elements <= b.elements
        return result

    @classmethod
    def is_uperset(self, a: MySet, b: MySet) -> bool:
        result = a.elements >= b.elements
        return result

    @classmethod
    def is_disjoint(self, a: MySet, b: MySet) -> bool:
        result = a.elements.isdisjoint(b.elements)
        return result

    @classmethod
    def is_same(self, a: MySet, b: MySet) -> bool:
        result = a.elements == b.elements
        return result

    @classmethod
    def make_direct_product(self, a: MySet, b: MySet) -> MySet:
        p_list = list(itertools.product(a.elements, b.elements))
        result = {MyElement(index=i, value=p) for i, p in enumerate(p_list)}
        return MySet(elements=result)
        

from typing import Set

from model.myelement import MyElement
from model.myset import MySet
from controller.myset_controller import MySetController


get_cap = MySetController.get_cap
get_cup = MySetController.get_cup
is_same = MySetController.is_same
make_direct_product = MySetController.make_direct_product


if __name__ == "__main__":
    universal_set_num: int = 10
    elements = set({MyElement(index=0), MyElement(index=1), MyElement(index=2)})
    universal_elements = {
        MyElement(index=i) for i in range(universal_set_num)
    }

    universal_set = MySet(elements=universal_elements)
    a = MySet(elements=set(list(universal_elements)[:3]))
    b = MySet(elements=set(list(universal_elements)[2:-1]))
    set_c = MySet(elements=set(list(universal_elements)[2:-2]))

    cap_ab = get_cap(a, b)
    cap_aa = get_cap(a, a)
    cup_ab = get_cup(a, b)
    cup_ba = get_cup(b, a)
    cup_aa = get_cup(a, a)
    cup_bc = get_cup(b, set_c)

    print("巾等律 A cup A = A: ", is_same(cup_aa, a))
    print("交換律 A cup B = B cup A: ", is_same(cup_ab, cup_ba))
    print(
        "結合律 (A cup B) cup C = A cup (B cup C): ",
        is_same(
            get_cup(cup_ab, set_c),
            get_cup(a, cup_bc)
        )
    )


    # 直積
    p_ab = make_direct_product(a, b)
    print(p_ab)

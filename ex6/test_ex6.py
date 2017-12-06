from ex6 import *

def test_small_1():
    assert part_1_and_2('0 2 7 0') == (4, 5)


def test_big_1():
    inputo = '4 1 15 12 0 9 9 5 5 8 7 3 14 5 12 3'
    assert part_1_and_2(inputo) == (2392, 6681)


from ex8 import *

inputo = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''

def test_part_1_1():
    assert part_1(inputo) == 1

def test_part_2_1():
    assert part_2(inputo) == 10

def test_part_1_2():
    assert part_1(open('inputo.txt', 'r').read() ) == 5849

def test_part_2_2():
    assert part_2(open('inputo.txt', 'r').read() ) == 6702

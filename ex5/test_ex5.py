from ex5 import *

inputito = """0
3
0
1
-3
"""

def test_jumping_1():
    inputo = np.array(inputito.splitlines(), dtype=np.int)
    assert escape_1(inputo) == 5

def test_jumping_2():
    inputo = np.array(inputito.splitlines(), dtype=np.int)
    assert escape_2(inputo) == 10

def test_part1():
    inputo = np.loadtxt('input.txt', dtype=np.int)
    assert escape_1(inputo) == 378980

def test_part2():
    inputo = np.loadtxt('input.txt', dtype=np.int)
    assert escape_2(inputo) == 26889114

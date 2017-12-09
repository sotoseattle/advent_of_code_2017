from ex7 import *

inputo = '''pbga (66)
    xhth (57)
    ebii (61)
    havc (66)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    qoyq (66)
    padx (45) -> pbga, havc, qoyq
    tknk (41) -> ugml, padx, fwft
    jptl (61)
    ugml (68) -> gyxo, ebii, jptl
    gyxo (61)
    cntj (57)'''

def test_root():
    assert root(inputo) == 'tknk'

def test_part_1():
    assert root(open('inputo.txt', 'r').read() ) == 'hlqnsbe'

def test_small_2():
    assert part_2(inputo) == 60

def test_part_2():
    assert part_2(open('inputo.txt', 'r').read()) == 1993


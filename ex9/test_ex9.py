from ex9 import *

def test_score():
    assert part_1('{}') == 1
    assert part_1('{{{}}}') == 6 # score of 1 + 2 + 3 = 6.
    assert part_1('{{},{}}') == 5 # score of 1 + 2 + 2 = 5.
    assert part_1('{{{},{},{{}}}}') == 16 # score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
    assert part_1('{<a>,<a>,<a>,<a>}') == 1 # score of 1.
    assert part_1('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9 # score of 1 + 2 + 2 + 2 + 2 = 9.
    assert part_1('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9 # score of 1 + 2 + 2 + 2 + 2 = 9.
    assert part_1('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3 # score of 1 + 2 = 3.

def test_part_1():
    assert part_1(open('inputo.txt', 'r').read() ) == 11089

def test_part_2():
    assert part_2(open('inputo.txt', 'r').read() ) == 5288

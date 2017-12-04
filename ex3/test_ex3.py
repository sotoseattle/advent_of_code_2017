from ex3 import *

def test_layer_I():
    layer = onion_ring(3)
    assert layer['sid'] == 3
    assert layer['max'] == 9
    assert layer['len'] == 8

def test_layer_II():
    layer = onion_ring(12)
    assert layer['sid'] == 5
    assert layer['max'] == 25
    assert layer['len'] == 16

def test_layer_III():
    layer = onion_ring(48)
    assert layer['sid'] == 7
    assert layer['max'] == 49
    assert layer['len'] == 24

def test_builder():
    sp = build_spiral(9) 
    assert sp[0,0] == 5.0
    assert sp[2,2] == 9.0

def test_adj():
    assert adjacent(0,0, 3, 3) == [[0, 0], [0, 1], [1, 0], [1, 1]]
    assert adjacent(2,0, 3, 3) == [[1, 0], [1, 1], [2, 0], [2, 1]]

def test_onion_dist():
    assert resolve_1(1) == 0
    assert resolve_1(2) == 1
    assert resolve_1(8) == 1
    assert resolve_1(3) == 2
    assert resolve_1(7) == 2
    assert resolve_1(20) == 3
    assert resolve_1(44) == 5
    assert resolve_1(289326) == 419

def test_resolve():
    assert resolve_2(9) == 10
    assert resolve_2(750) == 806
    assert resolve_2(289326) == 295229

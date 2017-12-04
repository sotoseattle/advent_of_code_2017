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

def test_onion_dist_I():
    assert onion_distance(1) == 0
    assert onion_distance(2) == 1
    assert onion_distance(8) == 1
    assert onion_distance(3) == 2
    assert onion_distance(7) == 2
    assert onion_distance(20) == 3
    assert onion_distance(44) == 5
    assert onion_distance(289326) == 419


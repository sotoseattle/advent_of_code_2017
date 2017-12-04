import numpy as np

def onion_ring(target):
    sol = {'sid': 1, 'max': 1, 'len': 1}
    while sol['max'] < target:
        len = (sol['sid'] * 4) + 4
        sol['sid'] += 2             # side length of square layer
        sol['max'] += len           # max value of the onion layer
        sol['len'] = len            # total number of digits in layer
    return sol

def build_spiral(n):
    '''Ugly as hell, should be refactored or redone'''
    data = onion_ring(n)
    max_side = data['sid']
    top_level = int((max_side - 1) / 2)
    spiral = np.zeros((max_side, max_side))
    spiral[top_level, top_level] = 1
    
    start_max = 2
    for level in range(1, top_level+1):
        data = onion_ring(start_max)
        start_max = data['max'] + 1

        z = data['sid']
        layer = [x for x in range(data['max'], data['max']-data['len'], -1)]
        layer.sort()
        layer.insert(0, layer[-1])
        sides = [layer[x:x+z] for x in range(0, len(layer), z-1)]
        a = top_level - int((z-1)/2)
        b = top_level + int((z-1)/2) + 1
        sides[0].reverse()
        spiral[a:b, b-1] = sides[0]
        sides[1].reverse()
        spiral[a, a:b] = sides[1]
        spiral[a:b, a] = sides[2]
        spiral[b-1, a:b] = sides[3]
    
    return spiral

def prune(i, length):
    base = [-1, 0, 1]
    if i < 1:
        del(base[0])
    if i >= length-1:
        del(base[-1])
    return base

def adjacent(i, j, I, J):
    return [[i+x, j+y] for x in prune(i, I) for y in prune(j, J)]

def resolve_1(target):
    sp = build_spiral(target)
    i, j = np.argwhere(sp == target)[0]
    mid = int((sp.shape[0] - 1) / 2)
    return abs(i - mid) + abs(j - mid)

def resolve_2(n):
    MAX_DIGIT = 100
    spiral = build_spiral(MAX_DIGIT)

    side = spiral.shape[0]
    sol = np.zeros((side, side))
    mid = int((side - 1) / 2)
    sol[mid, mid] = 1

    for x in range(1, int(spiral.max()+1)):
        i, j = np.argwhere(spiral == x)[0]
        val = int(sum([sol[a,b] for a,b in adjacent(i, j, side, side)]))
        if val > n:
            return val
        else:
            sol[i, j] = val
    return sol


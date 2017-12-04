def onion_ring(target):
    sol = {'sid': 1, 'max': 1, 'len': 1}
    while sol['max'] < target:
        len = (sol['sid'] * 4) + 4
        sol['sid'] += 2
        sol['max'] += len
        sol['len'] = len
    return sol

def onion_distance(target):
    if target == 1:
        return 0

    # extract the square layer of numbers that include the target
    data = onion_ring(target)
    b = [x for x in range(data['max'], data['max']-data['len'], -1)]

    # manipulate it to recreate each of the sides of the square
    b.sort()
    b.insert(0, b[-1])
    for x in range(0, len(b), data['sid']-1):
        side = b[x:x+data['sid']]
        if target in side:
            # level is the number of concentric layers away from 1
            level = (data['sid'] - 1) / 2
            midpoint = side[int((len(side)-1)/2)]
            # dist is the distance to the midpoint of the side
            dist = abs(target - midpoint)
            return  dist + level

    raise 'Malfunction brrrp!'

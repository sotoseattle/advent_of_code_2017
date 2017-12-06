import numpy as np
from itertools import count

def nexto(i, zen):
    return 0 if i == zen-1 else i+1

def part_1_and_2(inputo_str):
    '''return tuple (sol to part 2, sol to part 1)'''
    listo = [int(x) for x in inputo_str.split(r' ')]
    zen = len(listo)
    configurations = []
    for i in count():
        chuchu = str(listo) if listo else ''
        if chuchu in configurations:
            return ((len(configurations) - configurations.index(chuchu)), i)
        else:
            configurations.append(chuchu)
            listo = mise_en_place(listo, zen)
    raise 'badaboooom!'

def mise_en_place(arr, zen):
    '''get everything ready: select block to distribute and starting position'''
    i_max_load = np.argmax(arr)
    load = arr[i_max_load]
    arr[i_max_load] = 0
    return distribute(load, nexto(i_max_load, zen), arr, zen)

def distribute(load, i, arr, zen):
    '''cycle through until load is distributed'''
    while load > 0:
        arr[i] += 1
        i = nexto(i, zen)
        load -= 1
    return arr



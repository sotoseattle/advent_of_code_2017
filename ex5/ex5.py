import numpy as np

def escape_1(arr):
    position = 0
    steps = 0
    while position in range(0, arr.shape[0]):
        to_jump = arr[position]
        arr[position] += 1
        position += to_jump
        steps += 1

    return steps

def escape_2(arr):
    zen = arr.shape[0]
    position = 0
    steps = 0
    while position < zen:
        to_jump = arr[position]
        arr[position] += -1 if to_jump >= 3 else 1
        position += to_jump
        steps += 1

    return steps

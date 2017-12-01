import math

def captcha(arr, fun):
    zen = len(arr)
    tot = sum([int(arr[i]) for i in range(0, zen) if arr[i] == arr[fun(i, zen)]])
    return tot

def captcha_1(string_numbers):
    return captcha(string_numbers, lambda i, j: (i+j-1)%j)

def captcha_2(string_numbers):
    return captcha(string_numbers, lambda i, j: (i+math.ceil(j/2))%j)

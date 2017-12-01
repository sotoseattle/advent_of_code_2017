import math

def captcha(lnum, f):
    zen = len(lnum)
    tot = sum([int(lnum[i]) for i in range(0, zen)
               if lnum[i] == lnum[f(i, zen)]])
    return tot

def  captcha_1(string_numbers):
    lnum = list(string_numbers)
    return captcha(lnum, lambda i, j: (i+j-1)%j)

def captcha_2(string_numbers):
    lnum = list(string_numbers)
    return captcha(lnum, lambda i, j: (i+math.ceil(j/2))%j)

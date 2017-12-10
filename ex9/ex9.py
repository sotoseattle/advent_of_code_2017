import re
import sys
sys.setrecursionlimit(10_000)

def score(inputo, abierto=False, level=0, tot=0):
    if len(inputo) == 0:
        return tot

    char = inputo[0]
    inputo = inputo[1:]
    if char == '}':
        abierto = False
        tot += level
        level -= 1
    elif char == '{':
        level += 1
        abierto = True

    return score(inputo, abierto, level, tot)

def cleanup(inputo):
    inputo = re.sub(r'\!.', '', inputo)
    garbage = sum([len(e) for listo in re.findall(r'<([^>]*)>', inputo) for e in listo])
    inputo = re.sub(r'(<[^>]*>)', '', inputo)
    inputo = re.sub(r'[^{}]', '', inputo)
    return (inputo, garbage)

def part_1(inputo):
    return score(cleanup(inputo)[0])

def part_2(inputo):
    return cleanup(inputo)[1]

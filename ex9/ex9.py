import re
import sys
sys.setrecursionlimit(5_000)

def score(inputo, level=0, tot=0):
    if len(inputo) == 0: return tot

    if inputo[0] == '}':
        tot += level
        level -= 1
    elif inputo[0] == '{':
        level += 1

    return score(inputo[1:], level, tot)

def cleanup(inputo):
    inputo = re.sub(r'\!.', '', inputo)
    garbage = sum([len(e) for listo in re.findall(r'<([^>]*)>', inputo) for e in listo])
    inputo = re.sub(r'(<[^>]*>|[^{}])', '', inputo)
    return (inputo, garbage)

def part_1(inputo):
    return score(cleanup(inputo)[0])

def part_2(inputo):
    return cleanup(inputo)[1]

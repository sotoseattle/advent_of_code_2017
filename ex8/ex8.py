import re

def run_it(instructions):
    vars = {}
    maximos = []
    patt = re.compile('^(\w+)\s(inc|dec)\s(-?\d+)\sif\s(\w+)\s(.+)$')
    for line in instructions.splitlines():
        m = re.search(patt, line.strip())
        if m:
            if m.group(1) not in vars:
                vars[m.group(1)] = 0
            if m.group(4) not in vars:
                vars[m.group(4)] = 0
            n = int(m.group(3))
            n = -1*n if m.group(2)=='dec' else n
            if eval('{} {}'.format(vars[m.group(4)], m.group(5))):
                vars[m.group(1)] += n
                maximos.append(max(vars.values()))
    return {'final_max_val': maximos[-1], 'interim_max_val': max(maximos)}

def part_1(inputo):
    return run_it(inputo)['final_max_val']

def part_2(inputo):
    return run_it(inputo)['interim_max_val']

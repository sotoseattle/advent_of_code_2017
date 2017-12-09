import re

def build_code(instructions):
    orders = []
    vars = {}
    for line in instructions.splitlines():
        patt = re.compile('^(\w+)\s(inc|dec)\s(-?\d+)\sif\s(\w+)\s([><\!\=]+)\s(-?\d+)$', flags=re.M)
        m = re.search(patt, line.strip())
        if m:
            vars[m.group(1)] = vars[m.group(4)] = 0
            n = int(m.group(3))
            n = -1*n if m.group(2)=='dec' else n
            orders.append({'v': m.group(1), 'q': n, 'cond_v': m.group(4), 'cond_op': m.group(5), 'cond_n': int(m.group(6))})
    return (vars, orders)


def run_it(inputo):
    maximo = -1_000_000
    vars, orders = build_code(inputo)
    for o in orders:
        if eval('{} {} {}'.format(vars[o['cond_v']], o['cond_op'], o['cond_n'])):
            vars[o['v']] += o['q']
            top = max(vars.values())
            maximo = top if top > maximo else maximo

    return {'final_max_val': max(vars.values()), 'interim_max_val': maximo}

def part_1(inputo):
    return run_it(inputo)['final_max_val']

def part_2(inputo):
    return run_it(inputo)['interim_max_val']

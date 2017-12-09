import re
import networkx as nx
from collections import Counter

def lowest_frequency(listo):
    freqs = Counter(listo)
    return [k for k in freqs if freqs[k]==1][0]

def root(inputo): # this is enough to solve part 1
    return lowest_frequency(re.findall(r'[a-zA-Z]+', inputo))

def build_graph(inputo): # create a hash that works as a tree
    G = nx.DiGraph()
    for line in inputo.splitlines():
        m = re.search(r'^\s*([a-zA-Z]+)\s\((\d+)\)(?:(\s+\-\>\s)*)(.+)?$', line)
        if m:
            n = m.group(1)
            G.add_node(n, weight=int(m.group(2)), load=int(m.group(2))) 
            if m.group(4):
                for v in m.group(4).split(', '):
                     G.add_edge(n, v)
    return G

def part_2(inputo):
    G = build_graph(inputo)
    bfs_traversal = reversed(list(nx.bfs_successors(G, root(inputo))))

    for base, branches in bfs_traversal:
        for e in branches:
            loads_below = [G.node[e]['load'] for e in branches]
            if len(set(loads_below)) == 1:
                G.node[base]['load'] = G.node[base]['load'] + G.node[branches[0]]['load']
            else:
                bad_node = branches[loads_below.index(lowest_frequency(loads_below))]
                bad_load = G.node[bad_node]['load']
                branches.remove(bad_node)
                good_load = G.node[branches[0]]['load']
                return G.node[bad_node]['weight'] - (bad_load - good_load)
    return None

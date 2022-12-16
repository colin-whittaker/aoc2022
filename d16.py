#!/usr/bin/env python3.10
import sys
import functools

@functools.lru_cache(maxsize=None)
def max_flow(pos, done, time):
    if time <= 0:
        return 0
    best = 0
    if pos not in done:
        flow = (time-1) * valves[pos]['rate']
        new_done = tuple(sorted(done + (pos,)))
        if flow:
            for node in valves[pos]['nodes']:
                best = max(best, flow + max_flow(node,new_done, time-2))
    for node in valves[pos]['nodes']:
        best = max(best, max_flow(node, done, time-1))
    return best

@functools.lru_cache(maxsize=None)
def max_flow2(pos, done, time, elephant):
    if time <= 0:
        return 0
    best = 0
    if pos not in done:
        flow = (time-1) * valves[pos]['rate']
        new_done = tuple(sorted(done + (pos,)))
        if flow:
            for node in valves[pos]['nodes']:
                best = max(best, flow + max_flow2(node,new_done, time-2, elephant))
    for node in valves[pos]['nodes']:
        best = max(best, max_flow2(node, done, time-1, elephant))
    if time == 26 and not elephant:
        best = max(best, max_flow2('AA', done, 26, True))
    return best

if __name__ == '__main__':
    #do stuff
    valves = {}
    for line in list(line.rstrip() for line in sys.stdin):
        line = line.split(' ')
        rate = int(line[4].split('=')[1][:-1])
        nodes = [x[:-1] if ',' in x else x for x in line[9:]]
        valves[line[1]] = { 'rate':rate, 'nodes':nodes}
    print(max_flow('AA', (), 30))
    print(max_flow2('AA', (), 26, False))

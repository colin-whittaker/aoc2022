#!/usr/bin/env python3.10
import copy
import sys

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    crates = []
    instructions = []
    mode = 'crate'
    for line in lines:
        if line == '':
            mode = 'ins'
            continue
        if mode == 'crate':
            crates.append(line)
        else:
            line = line.split()
            instructions.append([int(line[1]),line[3],line[5]])
    labels = crates.pop().split()
    stacks = {}
    for stack in labels:
        stacks[stack] = []
    crates.reverse()
    for crate in crates:
        l = len(crate)
        p = 0 
        while p < l:
            c = crate[p:p+3][1]
            if c != ' ':
                stacks[labels[p//4]].append(c)
            p += 4
    stacks2 = copy.deepcopy(stacks)
    #print(stacks)
    #print(instructions)
    for q,s,d in instructions:
        while q > 0:
            stacks[d].append(stacks[s].pop())
            q -= 1
    result = []
    for label in labels:
        result.append(stacks[label].pop())
    print(''.join(result))
    stacks = stacks2
    for q,s,d in instructions:
        stacks[d].extend(stacks[s][len(stacks[s])-q:])
        stacks[s] = stacks[s][:len(stacks[s])-q]
    result = []
    for label in labels:
        result.append(stacks[label].pop())
    print(''.join(result))

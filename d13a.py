#!/usr/bin/env python3.10
import ast
import math
import functools
import sys

def check_pair(left,right):
    if type(left) == type(right) == int:
        if left < right: return -1
        elif left > right: return 1
        else: return 0
    elif type(left) == type(right) == list:
        for i in range(min(len(left),len(right))):
            result = check_pair(left[i],right[i])
            if result != 0:  return result
        if len(right) > len(left):
            return -1
        elif len(right) < len(left):
            return 1
        else: return 0
    elif type(left) == int:
        return check_pair([left],right)
    elif type(right) == int:
        return check_pair(left,[right])

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    pairs = [[]]
    pkts = [[[2]],[[6]]]
    for line in lines:
        if line == '':
            pairs.append([])
        else:
            pairs[-1].append( ast.literal_eval(line) )
            pkts.append(pairs[-1][-1])

    print(sum([i+1 for i in range(0,len(pairs)) if check_pair(pairs[i][0],pairs[i][1])==-1 ]))

    pkts = sorted(pkts, key=functools.cmp_to_key(check_pair))
    print(math.prod([i+1 for i,p in enumerate(pkts) if (p == [[2]] or p == [[6]])]))

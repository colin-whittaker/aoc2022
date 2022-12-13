#!/usr/bin/env python3.10
import ast
import math
import sys

def check_pair(left,right):
    if type(left) == type(right) == int:
        if left < right: return 1
        elif left > right: return -1
        else: return 0
    elif type(left) == type(right) == list:
        for i in range(min(len(left),len(right))):
            result = check_pair(left[i],right[i])
            if result != 0:  return result
        if len(right) > len(left):
            return 1
        elif len(right) < len(left):
            return -1
        else:
            return 0
    elif type(left) == int:
        return check_pair([left],right)
    elif type(right) == int:
        return check_pair(left,[right])

def pkt_sort(pkts):
    n = len(pkts)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if check_pair(pkts[j+1], pkts[j]) == 1:
                pkts[j],pkts[j+1] = pkts[j+1], pkts[j]

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    pairs = []
    pkts = [[[2]],[[6]]]
    left,right = None,None
    for line in lines:
        if line == '':
            pairs.append((left,right))
            left,right = None, None
            continue
        if left == None:
            left = ast.literal_eval(line)
            pkts.append(left)
        else:
            right = ast.literal_eval(line)
            pkts.append(right)
    score = 0
    for i in range(0,len(pairs)):
        if check_pair(*pairs[i]) == 1:
            score += i+1
    print(score)

    pkt_sort(pkts)
    print(math.prod([i+1 for i,p in enumerate(pkts) if (p == [[2]] or p == [[6]])]))

#!/usr/bin/env python3.10
import sys

def decode(l,t):
    for _ in range(t):
        for n,i in nums:
            idx = l.index((n,i))
            l.pop(idx)
            new = (idx+n)%len(l)
            if new == 0:
                l.append((n,i))
            else:
                l.insert(new,(n,i))
    l = [x[0] for x in l]
    idx = l.index(0)
    return l[(idx+1000)%len(l)]+l[(idx+2000)%len(l)]+l[(idx+3000)%len(l)]
 
if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    nums = [(int(line),i) for i,line in enumerate(lines)]
    l = nums.copy()
    print(decode(l,1))
    nums = [(x*811589153,i) for x,i in nums]
    l = nums.copy()
    print(decode(l,10))

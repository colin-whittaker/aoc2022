#!/usr/bin/env python3.10
import sys

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    r = 1
    results = [1]
    for line in lines:
        if line == 'noop':
            results.append(r)
        else:
            cmd,v = line.split(' ')
            v = int(v)
            results.extend([r,r])
            r += v
    i = 20
    s = 0
    while i <= len(results):
        s += i*results[i]
        i+=40
    print(s)
    pos=0
    screen = []
    for i in range(1,len(results)):
        if results[i]-1<=pos<=results[i]+1:
            screen.append('#')
        else:
            screen.append('.')
        pos += 1
        if i%40 == 0:
            pos = 0
            print(''.join(screen))
            screen = []


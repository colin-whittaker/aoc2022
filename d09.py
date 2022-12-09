#!/usr/bin/env python3.10
import sys

def move_rope(h_x,h_y,t_x,t_y):
    if (abs(h_x-t_x) == 1 and abs(h_y-t_y) == 2) or (abs(h_x-t_x) == 2 and abs(h_y-t_y) == 1):
        if h_x > t_x:
            t_x += 1
        else:
            t_x -= 1
        if h_y > t_y:
            t_y += 1
        else:
            t_y -= 1
    if abs(h_x-t_x) > 1:
        if h_x > t_x:
            t_x += 1
        else:
            t_x -= 1
    if abs(h_y-t_y) > 1:
        if h_y > t_y:
            t_y += 1
        else:
            t_y -= 1
    return t_x,t_y

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    h_x,h_y,t_x,t_y = (0,0,0,0)
    log = set()
    for line in lines:
        d,n = line.split()
        n = int(n)
        while n > 0:
            match d:
                case 'U':
                    h_y += 1
                case 'D':
                    h_y -= 1
                case 'R': 
                    h_x += 1
                case 'L':
                    h_x -= 1
            t_x,t_y = move_rope(h_x,h_y,t_x,t_y)
            log.add((t_x,t_y))
            n -= 1
    print(len(log))
    pos = [ (0,0) for x in range(0,10) ] 
    log = set()
    for line in lines:
        d,n = line.split()
        n = int(n)
        while n > 0:
            h_x,h_y = pos[0]
            match d:
                case 'U':
                    h_y += 1
                case 'D':
                    h_y -= 1
                case 'R': 
                    h_x += 1
                case 'L':
                    h_x -= 1
            pos[0] = (h_x,h_y)
            for i in range(0,9):
                h_x,h_y = pos[i]
                t_x,t_y = pos[i+1]
                pos[i+1] = (move_rope(h_x,h_y,t_x,t_y))
            log.add(pos[9])
            n -= 1
    print(len(log))

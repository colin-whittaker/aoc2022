#!/usr/bin/env python3.10
import sys

def snow_move(snow,edges):
    b = []
    for x,(i,j) in snow:
        match x:
            case '>': pos = (i,j+1)
            case '<': pos = (i,j-1)
            case 'v': pos = (i+1,j)
            case '^': pos = (i-1,j)
        if pos in edges:
            match x:
                case '>': pos = (i,1)
                case '<': pos = (i,len(lines[0])-2)
                case 'v': pos = (1,j)
                case '^': pos = (len(lines)-2,j)
        b.append((x,pos))
    return b, set(z for _,z in b)

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    start = (0,lines[0].index('.'))
    end   = (len(lines)-1,lines[-1].index('.'))
    edges = set([(-1,start[1]),(end[0]+1,end[1])])
    snow  = []
    for i,r in enumerate(lines):
        for j,c in enumerate(r):
            if c in '#':
                edges.add((i,j))
            elif c in '><v^':
                snow.append((c,(i,j)))

    state = {start}
    time  = 0
    while end not in state:
        time += 1
        new  = set()
        snow,snow_set = snow_move(snow,edges)
        for pos in state:
            possible = { (pos[0]+y,pos[1]+x) for (y,x) in [(0,1),(0,-1),(0,0),(1,0),(-1,0)] }
            new |= possible - snow_set - edges
        state = new
    print(time)
    state = {end}
    while start not in state:
        time += 1
        new  = set()
        snow,snow_set = snow_move(snow,edges)
        for pos in state:
            possible = { (pos[0]+y,pos[1]+x) for (y,x) in [(0,1),(0,-1),(0,0),(1,0),(-1,0)] }
            new |= possible - snow_set - edges
        state = new
    state = {start}
    while end not in state:
        time += 1
        new  = set()
        snow,snow_set = snow_move(snow,edges)
        for pos in state:
            possible = { (pos[0]+y,pos[1]+x) for (y,x) in [(0,1),(0,-1),(0,0),(1,0),(-1,0)] }
            new |= possible - snow_set - edges
        state = new
    print(time)

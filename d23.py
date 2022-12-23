#!/usr/bin/env python3.10
import sys
from collections import Counter

def grid_edges(grid):
    x1,x2,y1,y2 = 0,0,0,0
    for x,y in grid:
        x1,x2 = min(x1,x),max(x2,x)
        y1,y2 = min(y1,y),max(y2,y)
    return x1,x2,y1,y2

def print_grid(grid):
    x1,x2,y1,y2 = grid_edges(grid)
    for y in range(y1,y2+2):
        row = [grid[(x,y)] if (x,y) in grid else '.' for x in range(x1-1,x2+2)]
        print(''.join(row))
            
def test_move(elf,grid,r):
    d = [(0,-1),(0,1),(-1,0),(1,0)]
    test = [ [(-1,-1),(0,-1),(1,-1)],[(-1,1),(0,1),(1,1)],[(-1,-1),(-1,0),(-1,1)],[(1,-1),(1,0),(1,1)] ]
    x,y = elf
    v = True
    for t in test:
        for a,b in t:
            if (x+a,y+b) in grid:
                v = False
    if v:
        return None
    for i in range(r,r+4):
        v = True
        for a,b in test[i%4]:
            if (x+a,y+b) in grid:
                v = False
        if v:
            a,b = d[i%4]
            return (x+a,y+b)
    return None

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    grid={}
    for y,line in enumerate(lines):
        for x,c in enumerate(line):
            if c == '#':
                grid[(x,y)] = c 
    r = 0 
    while True:
        moves = {}
        for elf in grid:
            res = test_move(elf,grid,r)
            if res is not None:
                moves[elf] = res
        if len(moves) == 0:
            break
        clash = Counter(moves.values())
        for move,dest in moves.items():
            if clash[dest] == 1:
                del grid[move]
                grid[dest] = '#'
        if r == 9:
            x1,x2,y1,y2 = grid_edges(grid)
            print((x2+1-x1)*(y2+1-y1) - len(grid))
        r += 1
    print(r+1)

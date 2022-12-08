#!/usr/bin/env python3.10
import sys

def tree_visible(x,y,grid):
    max_x = len(line)
    max_y = len(grid)
    h = grid[y][x]
    if x == 0 or x == max_x -1:
        return True
    if y == 0 or y == max_y -1:
        return True
    # East 
    if len( [t for t in grid[y][x+1:] if t >= h]) == 0:
        return True
    # west
    if len([t for t in grid[y][0:x] if t >= h]) == 0:
        return True
    # north
    if len([t for r in grid[0:y] for t in r[x] if t >= h]) == 0:
        return True
    # south
    if len([t for r in grid[y+1:] for t in r[x] if t >= h]) == 0:
        return True
    return False

def tree_score(x,y,grid):
    max_x = len(line)
    max_y = len(grid)
    h = grid[y][x]
    if x == 0 or x == max_x -1:
        return 0
    if y == 0 or y == max_y -1:
        return 0
    e,w,n,s = (0,0,0,0)
    for i in range(x+1,max_x):
        e += 1
        if grid[y][i] >= h:
            break
    for i in range(x-1,-1,-1):
        w += 1
        if grid[y][i] >= h:
            break
    for j in range(y+1,max_y):
        s += 1
        if grid[j][x] >= h:
            break
    for j in range(y-1,-1,-1):
        n += 1
        if grid[j][x] >= h:
            break
    return e*w*n*s

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    grid = []
    for line in lines:
        grid.append([*line])
    visible = []
    max_x = len(line) 
    max_y = len(grid)
    for j in range(0,max_y):
        for i in range(0,max_x):
            if tree_visible(i,j,grid):
                visible.append((i,j))
    print(len(visible))
    scores = []
    for j in range(0,max_y):
        for i in range(0,max_x):
            scores.append(tree_score(i,j,grid))
    print(max(scores))

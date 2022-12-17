#!/usr/bin/env python3.10
import sys

shapes = [[(0,0),(1,0),(2,0),(3,0)], [(1,0),(0,1),(1,1),(2,1),(1,2)],[(0,0),(1,0),(2,0),(2,1),(2,2)],[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(0,1),(1,1)]]

def move_ok(grid, shape, xpos, ypos, move):
    a,b = move
    for x,y in shape:
        x,y = xpos+x+a,ypos+y+b
        if not 0<=x<=6 or y < 0 or (x,y) in grid:
            return False 
    return True

def print_grid(grid,max_y):
    for y in range(max_y,-1,-1): 
        row = []
        for x in range(7):
            row.append( grid[x,y] if (x,y) in grid else '.')
        print(''.join(['|']+row+['|']))
    print('+-------+')

def grid_cache_key(grid,max_y):
    key = []
    for x in range(7):
        for y in range(max_y,0,-1):
            if (x,y) in grid:
                key.append(str(max_y-y))
                break
    return ','.join(key)

if __name__ == '__main__':
    jet = list(line.rstrip() for line in sys.stdin)[0]
    jet_len = len(jet)
    jet_pos,rock,max_y = 0,0,0
    grid, cache = {}, {}
    height = [0]
    while True:
        xpos,ypos = 2, max_y+3
        shape = shapes[rock%5]
        while True:
            move = (-1,0) if jet[jet_pos] == '<' else (1,0)
            jet_pos = (jet_pos+1) % jet_len
            if move_ok(grid, shape, xpos, ypos, move):
                xpos += move[0]
            if move_ok(grid, shape, xpos, ypos, (0,-1)):
                ypos += -1
            else:
                for x,y in shape:
                    grid[(x+xpos,y+ypos)] = '#'
                    max_y = max(max_y,y+ypos+1)
                break
        rock += 1
        height.append(max_y)
        key = (rock%5,jet_pos,grid_cache_key(grid,max_y))
        if key in cache:
            old_rock,old_y=cache[key]
            for goal in [2022,1000000000000]:
                repeats = (goal - old_rock)//(rock-old_rock)
                extra_rocks = (goal - rock)%(rock-old_rock)
                print(repeats*(max_y-old_y)+height[old_rock+extra_rocks])
            break
        cache[key] = (rock,max_y)

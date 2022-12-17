#!/usr/bin/env python3.10
import sys

shapes = [[(0,0),(1,0),(2,0),(3,0)], [(1,0),(0,1),(1,1),(2,1),(1,2)],[(0,0),(1,0),(2,0),(2,1),(2,2)],[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(0,1),(1,1)]]

def move_ok(grid, shape, xpos, ypos, move):
    a,b = move
    for x,y in shape:
        x,y = xpos+x+a,ypos+y+b
        if not 0<=x<=6:
            return False 
        if y < 0:
            return False
        if (x,y) in grid:
            return False
    return True

def print_grid(grid,y):
    while y >= 0:
        row = ['|']
        for x in range(7):
            if (x,y) in grid:
                row.append(grid[x,y])
            else:
                row.append('.')
        row.append('|')
        print(''.join(row))
        y -= 1
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
    jet = list(line.rstrip() for line in sys.stdin)
    jet = jet[0]
    jet_len = len(jet)
    jet_pos = 0
    rock = 0
    max_y = 0
    grid = {}
    cache = {}
    height = [0]
    #do stuff
    while True:
        xpos = 2
        ypos = max_y+3
        stuck = False
        shape = shapes[rock%5]
        while not stuck:
            move = (-1,0) if jet[jet_pos] == '<' else (1,0)
            jet_pos = (jet_pos+1) % jet_len
            if move_ok(grid, shape, xpos, ypos, move):
                xpos += move[0]
            if move_ok(grid, shape, xpos, ypos, (0,-1)):
                ypos += -1
            else:
                stuck = True
                for x,y in shape:
                    grid[(x+xpos,y+ypos)] = '#'
                    max_y = max(max_y,y+ypos+1)
        rock += 1
        height.append(max_y)
        key = (rock%5,jet_pos,grid_cache_key(grid,max_y))
        if key in cache:
            old_rock,old_y=cache[key]
            goal = 2022
            repeats = (goal - old_rock)//(rock-old_rock)
            extra_rocks = (goal - rock)%(rock-old_rock)
            print(repeats*(max_y-old_y)+height[old_rock+extra_rocks])
            goal = 1000000000000
            repeats = (goal - old_rock)//(rock-old_rock)
            extra_rocks = (goal - rock)%(rock-old_rock)
            print(repeats*(max_y-old_y)+height[old_rock+extra_rocks])
            sys.exit()
        else:
            cache[key] = (rock,max_y)

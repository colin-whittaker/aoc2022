#!/usr/bin/env python3.10
import sys

def print_grid(grid,dims):
    x1,x2,y1,y2 = dims
    for y in range(y1,y2+1):
        row = []
        for x in range(x1,x2+1):
            if (x,y) in grid:
                row.append(grid[(x,y)])
            else:
                row.append('.')
        print(''.join(row))

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    grid = {}
    grid[(500,0)] = '+'
    xs,ys = [500],[0]
    for line in lines:
        points = line.split(' -> ')
        for start,end in zip(points, points[1:]):
            start_x,start_y = [int(i) for i in start.split(',')]
            end_x,end_y = [int(i) for i in end.split(',')]
            xs.extend([start_x,end_x])
            ys.extend([start_y,end_y])
            if start_x == end_x:
                for i in range(min(start_y,end_y),max(start_y,end_y)+1):
                    grid[(start_x,i)] = '#'
            else:
                for i in range(min(start_x,end_x),max(start_x,end_x)+1):
                    grid[(i,start_y)] = '#'
    dims = (min(xs),max(xs),min(ys),max(ys))
    print_grid(grid,dims)
    grains = 0
    escape = False
    while not escape:
        x,y = (500,0)
        while True:
            if (x,y+1) not in grid:
                y = y +1
            elif (x-1,y+1) not in grid:
                x,y = x-1,y+1
            elif (x+1,y+1) not in grid:
                x,y = x+1,y+1
            else:
                grid[(x,y)] = 'o'
                grains += 1
                break
            if not (dims[0]<=x<=dims[1] and dims[2]<=y<=dims[3]):
                escape = True
                break

    print(grains)
    grid = {key:val for key, val in grid.items() if val != 'o'}
    grains = 0
    escape = False
    x1,x2,y1,y2 = dims
    y2 += 1
    while not escape:
        x,y = (500,0)
        while True:
            x1 = x if x<x1 else x1
            x2 = x if x>x2 else x2
            if y == y2:
                grid[(x,y)] = 'o'
                grains +=1
                break
            if (x,y+1) not in grid:
                y = y +1
            elif (x-1,y+1) not in grid:
                x,y = x-1,y+1
            elif (x+1,y+1) not in grid:
                x,y = x+1,y+1
            else:
                grid[(x,y)] = 'o'
                grains += 1
                if (x,y) == (500,0):
                    escape = True
                break
    print(grains)

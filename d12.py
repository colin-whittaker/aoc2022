#!/usr/bin/env python3.10
import sys
import heapq

def valid_step(a,b):
    a = 0 if a == 'S' else ord(a) - ord('a')
    b = 25 if b == 'E' else ord(b) - ord('a')
    return True if a+1 >= b else False

def solve_grid(start,finish,grid):
    costs = [(0,(start))]
    visit = {}
    visit[start] = 0
    xmax,ymax = len(grid[0]),len(grid)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while True:
        if len(costs) == 0:
            return 10000000
        score, npos = heapq.heappop(costs)
        if npos == finish:
            return(score)
        x,y = npos
        for i,j in directions:
            a,b = x+i,y+j
            if 0 <= a < xmax and 0 <= b < ymax and valid_step(grid[y][x],grid[b][a]):
                if (a,b) not in visit or score+1 < visit[(a,b)]:
                    heapq.heappush(costs,(score+1,(a,b)))
                    visit[(a,b)] = score + 1

if __name__ == '__main__':
    grid = list(line.rstrip() for line in sys.stdin)
    #do stuff
    start, finish = None,None
    for y in range(0,len(grid)):
        if 'S' in grid[y]:
            start = (grid[y].find('S'),y)
        if 'E' in grid[y]:
            finish = (grid[y].find('E'),y)

    score = solve_grid(start,finish,grid)
    print(score)
    for y in range(0,len(grid)):
        for x in [i for i, letter in enumerate(grid[y]) if letter == 'a']:
            result = solve_grid((x,y),finish,grid)
            score = result if result < score else score
    print(score)

#!/usr/bin/env python3.10
import sys

def print_grid(grid,x,y):
    for j in range(y+1):
        print(''.join([grid[(i,j)] if (i,j) in grid else ' ' for i in range(x+1)]))

def moves(grid,steps,x,y,f,c=False):
    for move in steps:
        if move[-1].isalpha():
            moves= int(move[:-1])
            turn = move[-1]
        else:
            moves= int(move)
            turn = None
        i,j = d[f]
        for _ in range(moves):
            n = None
            if (x+i,y+j) in grid:
                xi,yj = x+i,y+j
            else:
                if not c:
                    rx,ry = d[(f+2)%4]
                    xi,yj = x,y
                    while (xi+rx,yj+ry) in grid:
                        xi,yj = xi+rx,yj+ry
                else:
                    if 50 <= x <= 99 and y == 0 and f == 3:
                        xi,yj,n = 0,x+100,0
                    elif 100 <= x <= 149 and y == 0 and f == 3:
                        xi,yj,n = x-100,199,3
                    elif x == 149 and 0 <= y <= 49 and f == 0:
                        xi,yj,n = 99,149-y,2
                    elif 100 <= x <= 149 and y == 49 and f == 1:
                        xi,yj,n = 99,x-50,2
                    elif 0 <= x <= 49 and y == 199 and f ==1:
                        xi,yj,n = 100+x,0,1
                    elif x == 49 and 150 <= y <= 199 and f == 0:
                        xi,yj,n = y-100,149,3
                    elif x == 99 and 100 <= y <= 149 and f == 0:
                        xi,yj,n = 149,149-y,2
                    elif x == 0 and 150 <= y <=199 and f == 2:
                        xi,yj,n = y-100,0,1
                    elif x == 50 and 0 <= y <=49 and f == 2:
                        xi,yj,n = 0,149-y,0
                    elif 0 <= x <= 49 and y == 100 and f == 3:
                        xi,yj,n = 50,50+x,0
                    elif x == 0 and 100 <= y <=149 and f == 2:
                        xi,yj,n = 50,149-y,0
                    elif x == 50 and 50 <= y <=99 and f == 2:
                        xi,yj,n = y-50,100,1
                    elif 50 <= x <= 99 and y == 149 and f == 1:
                        xi,yj,n = 49,100+x,2
                    elif x == 99 and 50 <= y <=99 and f == 0:
                        xi,yj,n = y+50,49,3
            if grid[(xi,yj)] == '.':
                x,y = xi,yj
                if n is not None:
                    i,j = d[n]
                    f = n
        if turn is not None:
            z = 1 if turn == 'R' else -1
            f = (f+z)%4
    return x,y,f

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    path = lines[-1]
    grid= {}
    max_x = 0
    for y,line in enumerate(lines[:-2]):
        for x,c in enumerate(line):
            if c != ' ':
                grid[(x,y)] = c
        max_x = max(max_x,x)
    max_y = y
    #print_grid(grid,max_x,max_y)
    for i in range(max_x+1):
        if (i,0) in grid and grid[(i,0)] == '.':
            startx = i
            break
    steps = []
    pos = 0 
    for i in range(len(path)):
        if path[i].isalpha():
            steps.append(path[pos:i+1])
            pos = i+1
    steps.append(path[pos:])
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    x,y,f = moves(grid,steps,startx,0,0)
    print(1000*(y+1) + 4*(x+1) + f)

    x,y,f = moves(grid,steps,startx,0,0,True)
    print(1000*(y+1) + 4*(x+1) + f)

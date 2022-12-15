#!/usr/bin/env python3.10
import sys

def mdist(ax,ay,bx,by):
    return abs(ax-bx)+abs(ay-by)

def empty_point(x,y,data):
    for s_x,s_y,b_x,b_y in data:
        if mdist(s_x,s_y,x,y) <= mdist(s_x,s_y,b_x,b_y):
            return False
    return True

def points_radius(x,y,d):
    xs = [i for i in range(x-d,x+d+1)]+[i for i in range(x+d-1,x-d,-1)]
    ys = [i for i in range(y,y+d+1)]+[i for i in range(y+d-1,y-d,-1)]+[i for i in range(y-d,0)]
    return(zip(xs,ys))

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    data=[]
    beacons = []
    yt,lim = 2000000,4000000
    #yt,lim = 10,20
    for line in lines:
        line = line.split(' ')
        s_x = int(line[2][2:-1])
        s_y = int(line[3][2:-1])
        b_x = int(line[8][2:-1])
        b_y = int(line[9][2:])
        data.append((s_x,s_y,b_x,b_y))
        if b_y == yt:
            beacons.append(b_y)

    roi = []
    for s_x,s_y,b_x,b_y in data:
        if s_y == yt:
            roi.append(s_x)
        dlim = mdist(s_x,s_y,b_x,b_y)
        dnew = mdist(s_x,s_y,s_x,yt)
        d = dlim - dnew
        if dnew <= dlim:
            roi.extend([x for x in range(s_x-d,s_x+d+1)])
    print(len(set(roi)-set(beacons)))
    for s_x,s_y,b_x,b_y in data:
        d = mdist(s_x,s_y,b_x,b_y)
        for x,y in points_radius(s_x,s_y,d+1):
            if 0<=x<=lim and 0<=y<=lim:
                if empty_point(x,y,data):
                    print(x*4000000+y)
                    sys.exit()

#!/usr/bin/env python3.10
import sys

sides = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    points = {}
    for line in lines:
        x,y,z = [int(i) for i in line.split(',')]
        points[(x,y,z)] = 6

    for x,y,z in points:
        for i,j,k in sides:
            if (x+i,y+j,z+k) in points:
                points[(x,y,z)] -= 1
    print(sum(points.values()))

    for pt in points:
        points[pt] = 6

    for x in range(-1,21):
        for y in range(-1,21):
            for z in range(-1,21):
                if (x,y,z) not in points:
                    points[(x,y,z)] = -1

    while True:
        found = []
        for x,y,z in points:
            if points[(x,y,z)] != -1:
                continue
            for i,j,k in sides:
                if (x+i,y+j,z+k) not in points:
                    found.append((x,y,z))
                    break
        if len(found):
            for pt in found:
                del points[pt]
        else:
            break

    for x,y,z in points:
        if points[(x,y,z)] == -1:
            continue
        for i,j,k in sides:
            if (x+i,y+j,z+k) in points :
                points[(x,y,z)] -= 1
    print(sum([i for i in points.values() if i != -1]))

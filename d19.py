#!/usr/bin/env python3.10
import sys
import functools
import math

def update_inv(inv, robots):
    return (inv[0]+robots[0],inv[1]+robots[1],inv[2]+robots[2],inv[3]+robots[3])

def afford_robot(inv, robots):
    return True if inv[0]>=robots[0] and inv[1]>=robots[1] and inv[2]>=robots[2] and inv[3]>=robots[3] else False

def deduct_inv(inv, robots):
    return (inv[0]-robots[0],inv[1]-robots[1],inv[2]-robots[2],0)

@functools.cache
def max_geode(blueprint,inv, robots, time):
    if time <= 0:
        return 0
    best = 0
    new_inv = update_inv(inv,robots)
    if afford_robot(inv,blueprint[3][0]):
        new_robots = update_inv(robots,blueprint[3][1])
        best = max(best,robots[3]+max_geode(blueprint,deduct_inv(new_inv,blueprint[3][0]),new_robots,time-1))
    elif afford_robot(inv,blueprint[2][0]):
        new_robots = update_inv(robots,blueprint[2][1])
        best = max(best,robots[3]+max_geode(blueprint,deduct_inv(new_inv,blueprint[2][0]),new_robots,time-1))
    else:
        best = robots[3]+max_geode(blueprint,deduct_inv(new_inv,(0,0,0,0)),robots,time-1)
        if afford_robot(inv,blueprint[0][0]) and blueprint[0][0][0] < time:
            new_robots = update_inv(robots,blueprint[0][1])
            best = max(best,robots[3]+max_geode(blueprint,deduct_inv(new_inv,blueprint[0][0]),new_robots,time-1))
        if afford_robot(inv,blueprint[1][0]):
            new_robots = update_inv(robots,blueprint[1][1])
            best = max(best,robots[3]+max_geode(blueprint,deduct_inv(new_inv,blueprint[1][0]),new_robots,time-1))
    return best

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    blueprints = {}
    for line in lines:
        line = line.split(' ')
        blueprints[int(line[1][:-1])] = ( ((int(line[6]),0,0,0),(1,0,0,0)), ((int(line[12]),0,0,0),(0,1,0,0)), ((int(line[18]),int(line[21]),0,0),(0,0,1,0)),((int(line[27]),0,int(line[30]),0),(0,0,0,1)))

    result = []
    for x in blueprints:
        result.append(x*max_geode(blueprints[x],(0,0,0,0),(1,0,0,0),24))
        max_geode.cache_clear()
    print(sum(result))
    p = 1 
    for x in [1,2,3]:
        r = max_geode(blueprints[x],(0,0,0,0),(1,0,0,0),32)
        max_geode.cache_clear()
        print(x,r,p)
    print(p)

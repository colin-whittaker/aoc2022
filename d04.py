#!/usr/bin/env python3.10
import sys

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    score = 0
    score2 = 0
    for line in lines:
        elf1,elf2 = line.split(',')
        e1_min,e1_max = elf1.split('-')
        e2_min,e2_max = elf2.split('-')
        e1_min,e1_max = int(e1_min),int(e1_max)
        e2_min,e2_max = int(e2_min),int(e2_max)
        if e2_min >= e1_min and e2_min <= e1_max and e2_max >= e1_min and e2_max <= e1_max:
            score += 1
        elif e1_min >= e2_min and e1_min <= e2_max and e1_max >= e2_min and e1_max <= e2_max:
            score += 1
        if e2_min >= e1_min and e2_min <= e1_max:
            score2 += 1
        elif e1_min >= e2_min and e1_min <= e2_max:
            score2 += 1

    print(score)
    print(score2)

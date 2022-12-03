#!/usr/bin/env python3.10
import sys

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    score = 0
    for line in lines:
        l = int(len(line)/2)
        a = set(line[:l])
        b = set(line[l:])
        item = a.intersection(b).pop()
        if item.islower():
            score += ord(item) - ord('a') +1
        else:
            score += ord(item) - ord('A') +27
    print(score)

    score = 0
    for i in range(0,len(lines),3):
        a = set(lines[i])
        b = set(lines[i+1])
        c = set(lines[i+2])
        item = a.intersection(b,c).pop()
        if item.islower():
            score += ord(item) - ord('a') +1
        else:
            score += ord(item) - ord('A') +27
    print(score)


#!/usr/bin/env python3.10
import sys

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    for line in lines:
        for pos in range(0, len(line)):
            if len(set(line[pos:pos+4])) == 4:
                print(pos+4)
                break
    for line in lines:
        for pos in range(0, len(line)):
            if len(set(line[pos:pos+14])) == 14:
                print(pos+14)
                break

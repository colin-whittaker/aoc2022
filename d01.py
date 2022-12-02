#!/usr/bin/env python3.10
import sys

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    elves = []
    elf = 0
    for line in lines:
        if line == '':
            elves.append(elf)
            elf = 0
            continue
        elf += int(line)
    elves.append(elf)
    print(max(elves))
    print(sum(sorted(elves)[-3:]))

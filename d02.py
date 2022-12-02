#!/usr/bin/env python3.10
import sys

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    rounds = []
    for line in lines:
        rounds.append(line.split())

    score = 0
    for rnd in rounds:
        a = ord(rnd[0]) - ord('A')
        b = ord(rnd[1]) - ord('X')
        score += b+1
        if a == b:
            score += 3
        elif b == a +1:
            score +=6
        elif b == 0 and a == 2:
            score += 6
    print(score)

    score = 0
    for rnd in rounds:
        a = ord(rnd[0]) - ord('A')
        b = ord(rnd[1]) - ord('X')
        if b == 0: #lose
            score += (a + 2)%3+1
        elif b == 1: #draw
            score += a+1+3
        elif b == 2: #win
            score += (a+4)%3+6+1

    print(score)

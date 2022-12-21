#!/usr/bin/env python3.10
import sys

def solve_monkey(name):
    if len(monkeys[name]) == 1:
        return int(monkeys[name][0])
    a = solve_monkey(monkeys[name][0])
    b = solve_monkey(monkeys[name][2])
    match monkeys[name][1]:
        case '+': return a + b
        case '-': return a - b
        case '*': return a * b
        case '/': return a // b
    print('Error:', name, monkeys[name])

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    monkeys = {}
    for line in lines:
        line = line.split(' ')
        monkeys[line[0][:-1]] = line[1:]

    print(solve_monkey('root'))
    monkeys['root'][1] = '-'
    
    x = min_x = 1
    max_x = None
    monkeys['humn'][0] =  x
    while True:
        res = solve_monkey('root') 
        if res == 0: break
        if res < 0:
            max_x = x 
        else:
            min_x = x
        if max_x is None:
            x *= 2
        else:
            x = min_x + (max_x-min_x)//2 -1
        monkeys['humn'][0] =  x
    print(x)

#!/usr/bin/env python3.10
import math
import sys

def inspect(item,operation,d=0):
    op,v = operation
    if v =='old':
        v = item
    else:
        v = int(v)
    match op:
        case '+':
            item = item + v
        case '*':
            item = item * v
    return (item % d) if d else (item//3)

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    items = []
    items2 = []
    operation  = []
    test = []
    action_t = []
    action_f = []
    for line in lines:
        if 'items' in line:
            items.append([int(x) for x in line.split(':')[1].split(',')])
            items2.append([int(x) for x in line.split(':')[1].split(',')])
        elif 'Operation' in line:
            operation.append(line.split('=')[1].split(' ')[-2:])
        elif 'Test' in line:
            test.append(int(line.split(' ')[-1]))
        elif 'true' in line:
            action_t.append(int(line.split(' ')[-1]))
        elif 'false' in line:
            action_f.append(int(line.split(' ')[-1]))

    count= [0 for m in items]
    for r in range(0,20):
        for monkey in range(0, len(items)):
            while len(items[monkey]):
                item = inspect(items[monkey].pop(0),operation[monkey])
                count[monkey] += 1
                if item%test[monkey] == 0:
                    items[action_t[monkey]].append(item)
                else:
                    items[action_f[monkey]].append(item)
    count.sort()
    print(count[-2]*count[-1])

    items = items2
    count= [0 for m in items]
    d = math.prod(test)
    for r in range(0,10000):
        for monkey in range(0, len(items)):
            while len(items[monkey]):
                item = inspect(items[monkey].pop(0),operation[monkey],d)
                count[monkey] += 1
                if item%test[monkey] == 0:
                    items[action_t[monkey]].append(item)
                else:
                    items[action_f[monkey]].append(item)
    count.sort()
    print(count[-2]*count[-1])

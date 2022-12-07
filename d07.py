#!/usr/bin/env python3.10
import sys

def sum_dir(tree):
    global total
    global sizes
    size = 0
    for d in tree['children'].values():
        size += sum_dir(d)
    for n,s in tree['files']:
        size += s
    if size <= 100000:
        total += size
    sizes.append(size)
    return size

if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    root = {'children':{} , 'files':[]}
    stack = []
    cur = None
    for line in lines:
        if line == '$ cd /':
            cur = root
            continue
        if line == '$ ls':
            continue
        if '$ cd ' in line:
            new  = line.split()[2]
            if new == '..':
                cur = stack.pop()
            else:
                stack.append(cur)
                cur = cur['children'][new]
            continue
        a,b = line.split()
        if a == 'dir':
            cur['children'][b] = {'children':{} , 'files':[]}
            continue
        else:
            cur['files'].append((b,int(a)))
            continue
        print('unknown line:',line)
        sys.exit()
    total = 0
    sizes = []
    used = sum_dir(root)
    print(total)
    needed = 30000000-(70000000-used)
    sizes.sort()
    for size in sizes:
        if size >=  needed:
            print(size)
            break

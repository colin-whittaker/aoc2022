#!/usr/bin/env python3.10
import sys

def convertnum(num):
    num = reversed(num)
    result = 0
    for i,n in enumerate(num):
        match n:
            case '-': n = -1
            case '=': n = -2
        n = int(n)
        result += n * pow(5,i)
    return result

def convertsnafu(num):
    d2s = {0:'0',1:'1',2:'2',3:'=',4:'-'}
    snafu = ''
    while num:
        num, r = divmod(num,5)
        snafu += d2s[r]
        if r > 2:
            num +=1
    return snafu[::-1] if snafu else '0'
    
if __name__ == '__main__':
    lines = list(line.rstrip() for line in sys.stdin)
    #do stuff
    result = 0
    for line in lines:
        result += convertnum(line)
    print(result,convertsnafu(result))

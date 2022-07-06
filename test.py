import math
import sys

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    p = [x1, y1]
    q = [x2, y2]
    
    d = math.dist(p,q)
    
    sub = abs(r2-r1)
    add = r2+r1
    
    if d == 0:
        if r1 != r2:
            print('0')
        elif r1 == r2:
            print('-1')
    else:
        if d == add or d == sub:
            print('1')
        elif sub < d < add:
            print('2')
        elif d > add or d < sub:
            print('0')
    
    
# 1. 두 점의 거리가 r1+r2 크다
# 
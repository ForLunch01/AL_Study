from math import factorial
import sys
from itertools import combinations as cb


TC = int(sys.stdin.readline())

for _ in range(TC):
    N, M = map(int, sys.stdin.readline().split())
    res = factorial(M)/(factorial(N)*factorial(M-N))
    
    print(int(res))
    
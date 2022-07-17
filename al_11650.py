import sys

N = int(sys.stdin.readline())

coords = [[0,0] for i in range(N)]

for i in range(N):
    coords[i] = list(map(int, sys.stdin.readline().split()))
    
coords.sort()

for i in coords:
    print(*i)
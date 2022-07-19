# 독일 로또 {1,2,...,49}에서 6개
from itertools import combinations as cb

T_list = [-1]
while True:
    T_list = list(map(int, input().split()))
    if T_list[0] == 0:
        break
    for c in cb(T_list[1:], 6):
        print(*list(c))
    print()
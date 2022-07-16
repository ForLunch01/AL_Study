# 숫자 카드, 정수 하나
# 숫자 카드 N개
# 정수 M개가 주어졌을 때, 이 숫자 카드를 상근이가 갖고 있는지

import sys

N = int(sys.stdin.readline())
N_list = []
N_list.extend(map(int, sys.stdin.readline().split()))

N_dict = {}
for i in range(N):
    N_dict[N_list[i]] = i

M = int(sys.stdin.readline())
M_list = []
M_list.extend(map(int, sys.stdin.readline().split()))

for m in M_list:
    if m in N_dict:
        print(1, end=" ")
    else:
        print(0, end=" ")
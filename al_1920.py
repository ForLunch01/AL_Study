# N개의 정수 A[1], A[2], ..., A[N]
# 이 안에 X라는 정수가 존재하는가

from cmath import pi
import sys

N = int(sys.stdin.readline())
N_list = []
N_list.extend(map(int, sys.stdin.readline().split()))

# dictionary와 list의 in(Containment) 메소드 시간 복잡도 차이
N_dict = {}
for i in range(N):
    N_dict[N_list[i]] = i

M = int(sys.stdin.readline())
M_list = []
M_list.extend(map(int, sys.stdin.readline().split()))

for m in M_list:
    if m in N_dict:
        print(1)
    else:
        print(0)
    
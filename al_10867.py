import sys

input = sys.stdin.readline

N = int(input())

N_list = list(map(int, input().split()))
N_list = list(set(N_list))
N_list = sorted(N_list)

for i in range(len(N_list)):
    print(N_list[i], end=" ")
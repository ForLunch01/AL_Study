# N개의 정수로 이루어진 수열
# 크기가 양수인 부분수열 중,
# 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수

import sys
from itertools import combinations as cb

N, S = map(int, sys.stdin.readline().split())
N_list = []
N_list.extend(list(map(int, sys.stdin.readline().split())))

count = 0

# 정수 집합 N_list에서의 for문
for i in range(1, N+1):
    # 조합을 활용, 집합 N에서 1개를 고른 집합, 2개를 고른, ..., N개를 고른 집합
    for cb_element in cb(N_list,i):
        # 각 집합 원소의 합이 실제 S인 경우
        if sum(cb_element) == S:
            count += 1
print(count)
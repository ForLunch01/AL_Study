# 총 N개의 문자열의 집합 S
# 총 M개의 문자열
# M개의 문자열 중 S에 포함되어 있는 것은 몇 개인가?

# N, M을 입력 받음

import sys

N, M = map(int, sys.stdin.readline().split())


# S 입력 받음
# S = []
# for i in range(N):
#     S.append(input())

S = []
for i in range(N):
    S.append(sys.stdin.readline().strip())

S_dict = {}

for i, s in enumerate(S):
    S_dict[s] = i

# M 개의 문자열, T 입력 받음
T = []
for i in range(M):
    T.append(sys.stdin.readline().strip())
    
# 문자열 M, for문
cnt = 0
for m in T:
    if m in S:
        cnt += 1
        
print(cnt)
# 정수 집합 S
# A <= x <= B 인 모든 x가 S에 속하지 않음
# S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수

# 1. 집합의 크기
# 2. 집합 원소
# 3. n

import sys

L = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())

count = 0

if n in S:
    count = 0
else:
    S.append(n)
    S.sort()
    n_idx = S.index(n)
    
    if n_idx == 0:
        min = n
        max = S[n_idx+1]
        
        for i in range(min, max):
            for j in range(i+1, max):
                count += 1
        
    else:
        min = S[n_idx-1]
        max = S[n_idx+1]
    
        for i in range(min+1, n+1):
            for j in range(n, max):
                if i != j:
                    count += 1
    

print(count)




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


if n in S:
    print(0)
else:
    S.append(n)
    S = [0] + S
    S.sort() 

    n_idx = S.index(n)
    
    min = S[n_idx-1]
    max = S[n_idx+1]
  
    max -= 1                   
    min += 1
    print((n-min)*(max-n+1) + (max-n))
    
# (10보다 작은 수의 개수) * (10을 포함한 10보다 큰 수의 개수) + (10보다 큰 수의 개수)
    
    




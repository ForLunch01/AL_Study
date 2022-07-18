# 문제 해결 방법
# 1. N 크기를 가지는 Deque 생성
# 2. Deque[0]의 값이 뽑으려는 수 pos_list[0]과 같으면 추출 ***매우 중요, 뽑았으면 break
# 3. 아니라면 왼쪽 또는 오른쪽으로 Deque를 회전시켜야 함
# 4. 이동할 거리 계산 : len(Deque) / 2 >= Deque.index[pos_list[i]] 이면 왼쪽 회전, 아니면 오른쪽 회전


import sys
# deque import
from collections import deque


N, M = map(int, sys.stdin.readline().split())
pos_list = list(map(int, sys.stdin.readline().split()))

# deque 선언
deque_list = deque([i for i in range(1,N+1)])
cnt = 0

for i in range(M):
    while True:
        if deque_list[0] == pos_list[i]:
            deque_list.popleft()
            break
        else:
            print(deque)
            if len(deque_list)/2 >= deque_list.index(pos_list[i]):
                deque_list.rotate(-1)
                cnt += 1
            else:
                deque_list.rotate(+1)
                cnt += 1
            
print(cnt)



from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    N_deque = deque()
    
    for i in range(N):
        N_deque.append([N_list[i], i])
        
    print(N_deque)
        
    cnt = 0 
    while True:
        pop_element = [-1, -1]
        if N_deque[0][0] == max(N_list):
            pop_element = N_deque.popleft()
            N_list.remove(max(N_list))
            cnt += 1
        else:
            N_deque.rotate(-1)
        
        if pop_element[1] == M:
            break
    print(cnt)
    
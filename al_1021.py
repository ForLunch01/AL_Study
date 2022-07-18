import sys

N, M = map(int, sys.stdin.readline().split())
pos_list = list(map(int, sys.stdin.readline().split()))

cnt = 0

for m in range(M):
    if pos_list[m] == 1:
        N = N-1
    else:
        shift_num1 = pos_list[m] + 1
        shift_num2 = N - pos_list[m] + 1
        
        if shift_num1 < shift_num2:
            cnt += shift_num1
            for i in range(M):
                pos_list[i] = pos_list[i] - shift_num1
                if pos_list[i] <= 0:
                    pos_list[i] = pos_list[i] + N                        
        else:
            cnt += shift_num2
            for i in range(M):
                pos_list[i] = pos_list[i] + shift_num2
                if pos_list[i] > N:
                    pos_list[i] = pos_list[i] - N  
                                   
        if pos_list[m] == 1:
            N = N-1
            
print(cnt)
        



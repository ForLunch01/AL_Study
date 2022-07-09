N, M = map(int, input().split())

rect = []
for i in range(N):
    rect.append(list(map(int, input())))
    
s_sum_list = []

low_len = min(N, M)

for s in range(low_len):
    
    for i in range(N-s):
        for j in range(M-s):
                
            if rect[i][j] == rect[i+s][j] == rect[i][j+s] == rect[i+s][j+s]:
                s_sum_list.append((s+1)*(s+1))
                
print(max(s_sum_list))
import sys

N, M = map(int, sys.stdin.readline().split())

p_name_list = []

p_dict_name_is_key = {}
p_dict_num_is_key = {}

for i in range(N):
    p_name_list.append(sys.stdin.readline().strip())

for i in range(N):
    p_dict_num_is_key[i+1] = p_name_list[i]
    p_dict_name_is_key[p_name_list[i]] = i+1


for i in range(M):
    test = sys.stdin.readline().strip()
    
    if test.isdigit():
        print(p_dict_num_is_key[int(test)])
    else:
        print(p_dict_name_is_key[test])
    


        
    
    

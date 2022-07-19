import sys
from math import gcd

N = int(sys.stdin.readline())
N_list = []
N_len_list = []

for i in range(N):
    N_list.append(int(sys.stdin.readline()))
    
for j in range(1, N):
    N_len_list.append(N_list[j]-N_list[j-1])
    
tree_len = gcd(*N_len_list)
tree_len_max = N_list[-1]-N_list[0]
tree_count = tree_len_max//tree_len + 1 - len(N_list)

print(tree_count)
    




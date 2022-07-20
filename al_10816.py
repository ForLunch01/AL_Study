# 

import sys

input = sys.stdin.readline

M = int(input())
m_list = []
m_list.extend(list(map(int, input().split())))
N = int(input())
n_list = []
n_list.extend(list(map(int, input().split())))
n_dict = {}

for m in m_list:
    if m in n_dict:
        n_dict[m] += 1
    else:
        n_dict[m] = 1
        
for i in n_list:
    if i in n_dict:
        print(n_dict[i], end=" ")
    else:
        print(0, end=" ")

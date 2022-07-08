import sys
from itertools import combinations as cb

N, M = map(int, sys.stdin.readline().split())
card_list = list(map(int, sys.stdin.readline().split()))

card_list.sort()
card_sum_set = set()

for i in list(cb(card_list, 3)):
    card_sum_set.add(sum(i))

card_sum = list(card_sum_set)
card_sum_down = []

for i in range(len(card_sum)):
    if card_sum[i] <= M:
        card_sum_down.append(card_sum[i])
        
print(max(card_sum_down))
import sys

TC = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
_arr = [0] * len(arr)

count_val = 0

for i in range(len(arr)):
    update_index = arr.index(min(arr))
    _arr[update_index] = count_val
    count_val += 1
    arr[update_index] = 1001
    
for i in _arr:
    print(i, end=' ')

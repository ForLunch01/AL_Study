import sys

len_arr = int(sys.stdin.readline())
arr_A = list(map(int,sys.stdin.readline().split()))
arr_B = list(map(int,sys.stdin.readline().split()))

arr_A.sort()

res = 0

for i in range(len(arr_B)):
    res = res + max(arr_B)*arr_A[i]
    max_index = arr_B.index(max(arr_B))
    arr_B[max_index] = 0

print(res)
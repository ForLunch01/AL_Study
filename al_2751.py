import sys

N = int(sys.stdin.readline())

num_list = []

for i in range(N):
    num_list.append(int(sys.stdin.readline()))

# def partition(l, r, nums):
#     pivot, ptr = nums[r], l
#     for i in range(l, r):
#         if nums[i] <= pivot:
#             nums[i], nums[ptr] = nums[ptr], nums[i]
#             ptr += 1
#     nums[ptr], nums[r] = nums[r], nums[ptr]
#     return ptr
 
# def quicksort(l, r, nums):
#     if len(nums) == 1: 
#         return nums
#     if l < r:
#         pi = partition(l, r, nums)
#         quicksort(l, pi-1, nums)  
#         quicksort(pi+1, r, nums)
#     return nums

# def mergeSort(arr):
#     if len(arr) > 1:

#         mid = len(arr)//2
#         L = arr[:mid]
#         R = arr[mid:]
 
#         mergeSort(L)
#         mergeSort(R)
 
#         i = j = k = 0

#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1

#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
 
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1


# mergeSort(num_list)
num_list.sort()

for i in range(N):
    print(num_list[i])

N = int(input())

num_list = []

func_mem = [1, 2, 4, 7]

for i in range(N):
    num_list.append(int(input()))
    
for n in range(1, 11):
    if n >= 5:
        func_mem.append(func_mem[n-2] + func_mem[n-3] + func_mem[n-4])

    
for i in num_list:
    print(func_mem[i-1])

# N = int(input())

# num_list = []

# for i in range(N):
#     num_list.append(int(input()))
    
# def func_1_2_3(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 4
    
#     return func_1_2_3(n-3) + func_1_2_3(n-2) + func_1_2_3(n-1)

# for n in num_list:
#     print(func_1_2_3(n))



            

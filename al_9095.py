N = int(input())

num_list = []

func_mem = [1, 2, 4, 7]

for i in range(N):
    num_list.append(int(input()))
    
for n in range(1, 11):
    if n >= 5:
        print(n)
        func_mem.append(func_mem[n-2] + func_mem[n-3] + func_mem[n-4])
        print(n)
    
for i in num_list:
    print(func_mem[i-1])




            

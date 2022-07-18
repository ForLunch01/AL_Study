# f(1) = 1
# f(2) = 2
# f(3) = 3
# f(4) = 5
# f(n) = f(n-1) + f(n-2)

n = int(input())

memoi_list = [1, 2]

def double_x_n(num):   
    for i in range(1001):
        if len(memoi_list) < i:
            memoi_list.append(memoi_list[i-2] + memoi_list[i-3])
        if i == n:
            break
            
double_x_n(n)
print(memoi_list[n-1]%10007)
    
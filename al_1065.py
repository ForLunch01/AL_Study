N = int(input())

count = 0

def is_hansu(num):
    num_list = list(map(int, str(num)))
    for i in range(2, len(num_list)):
        if num_list[i] - num_list[i-1] != num_list[i-1] - num_list[i-2]:
            return False
    return True

for i in range(1, N+1):
    if i <= 99:
        count += 1
    else:
        count = count + int(is_hansu(i))
        
print(count)
    
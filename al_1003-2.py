import sys

N = int(sys.stdin.readline())

num_list = []

for i in range(N):
    num_list.append(int(sys.stdin.readline()))

fib_0_1 = [[0, 0] for i in range(41)]
fib_0_1[0] = [1, 0]
fib_0_1[1] = [0, 1]

for i in range(41):
    if i >= 2:
        fib_0_1[i][0] = fib_0_1[i-1][0]+fib_0_1[i-2][0]
        fib_0_1[i][1] = fib_0_1[i-1][1]+fib_0_1[i-2][1]

for i in num_list:
    print(*fib_0_1[i])
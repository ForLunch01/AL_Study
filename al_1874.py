# 첫 줄에 n이 주어짐
# 둘째 줄부터 n개의 줄에는 수열을 이루는
# 1 이상 n 이하의 정수가 하나씩 순서대로 주어짐
# 입력된 수열을 만들기 위한 스택 연산을 한 줄에 한 개씩 출력
# push => +, pop => -
# 불가능한 경우에는 NO를 출력한다.

# 다시 풀어보기

import sys

N = int(sys.stdin.readline())
N_stack = []
for i in range(N):
    N_stack.append(int(sys.stdin.readline()))

stack_count = 1    
temp = True
stack_list = []
op_list = []

for n in N_stack:
    while stack_count <= n:
        stack_list.append(stack_count)
        stack_count += 1
        op_list.append('+')
            
    if stack_list[-1] == n:
            stack_list.pop()
            op_list.append('-')
    else:
        temp = False
        break
    
if temp == False:
    print("NO")
else:
    for i in op_list:
        print(i)
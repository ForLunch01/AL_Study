N = int(input())

operation_list = []
stack = []

for i in range(N):
    operation_list.append(input())
    
    
for op in operation_list:
    op_first = op.split(" ")[0]
    
    if op_first == 'push':
        push_obj = int(op.split(" ")[1])
        stack.append(push_obj)
    elif op_first == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            pop_obj = stack.pop()
            print(pop_obj)
    elif op_first == 'size':
        print(len(stack))
    elif op_first == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif op_first == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    

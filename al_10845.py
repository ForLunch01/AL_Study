import sys

N = int(sys.stdin.readline())

oper_list = []
queue_test = []

for i in range(N):
    oper_list.append(sys.stdin.readline().strip())
    
def queue_oper(str, queue):
    if str.split()[0] == 'push':
        return queue_push(int(str.split()[1]), queue)
    
    elif str.split()[0] == 'pop':
        return queue_pop(queue)
    
    elif str.split()[0] == 'size':
        return queue_size(queue)
    
    elif str.split()[0] == 'empty':
        return queue_empty(queue)
    
    elif str.split()[0] == 'front':
        return queue_front(queue)
    
    elif str.split()[0] == 'back':
        return queue_back(queue)              

def queue_push(n, queue):
    queue.append(n)

def queue_pop(queue):
    if queue_empty(queue):
        return -1
    else:
        pop_value = queue[0]
        queue[:] = queue[1:]
        return pop_value


def queue_size(queue):
    return len(queue)

def queue_empty(queue):
    if len(queue) == 0:
        return 1
    else:
        return 0

def queue_front(queue):
    if queue_empty(queue):
        return -1
    else:
        return queue[0]

def queue_back(queue):
    if queue_empty(queue):
        return -1
    else:
        return queue[-1]

for i in range(N):
    r_val = queue_oper(oper_list[i], queue_test)
    if r_val != None:
        print(r_val)
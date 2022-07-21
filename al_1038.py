# 음이 아닌 정수 X
# 가장 큰 자릿수부터 작은 자릿수까지 감소
# 감소하는 수의 최대값은 9876543210
from itertools import combinations as cb

def check_decrease():
    N = int(input())
    numbers = [i for i in range(10)]
    list_num = []
    for i in range(1, 11):
        for c in cb(numbers, i):
            list_c = list(c)[::-1]
            list_num.append(int("".join(list(map(str, list_c)))))
    list_num.sort()
    
    try :
        print(list_num[N])
    except :
        print(-1)
check_decrease()
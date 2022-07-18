# 음이 아닌 정수 X
# 가장 큰 자릿수부터 작은 자릿수까지 감소
# 조합을 활용해보면 어떨까? 이 코드는 시간초과 났다...
def check_decrease(num):
    num_list = list(map(int, list(str(num))))
    for i in range(len(num_list)-1):
        if num_list[i] <= num_list[i+1]:
            return False
    else:
        return True

N = int(input())
i = 0
data = []
while N+1:
    if N >= 1023:
        break
    if i // 10 == 0:
        data.append(i)
        N = N-1
    else:
        if check_decrease(i):
            data.append(i)
            N = N-1
    i = i+1

if N >= 1023:
    print(-1)
else:
    print(data[N])


# N과 L이 주어진다.
# 합이 N
# 길이는 적어도 L
# 가장 짧은, 연속된, 음이 아닌
# 정수 리스트


N, L = map(int, input().split())

# def func():  
#     for i in range(L, 101):
#         for x in range(1000000000):
#             if sum(range(x, x+i)) > N:
#                 break
#             elif sum(range(x, x+i)) == N:
#                 print(*range(x, x+i))
#                 return       
#     else:
#         print(-1)

# func()


for i in range(L, 101):
    x = ((2*N/i) + 1 - i)/2 # 등차수열의 합 공식으로 x를 구함
    if x >= 0 and x % 1 == 0: # x는 0 이상의 정수
        print(*range(int(x), int(x+i)))
        break
else:
    print(-1)
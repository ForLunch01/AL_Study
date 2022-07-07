import sys

sugar = int(sys.stdin.readline())

count = 0

# 설탕의 양이 0 이상일 경우에만 while문 동작
while sugar >= 0:
    
    # 설탕의 5의 배수이면
    if sugar % 5 == 0:
        # 현재 count에 5로 나눈 몫을 더한 값이 총량임
        count += sugar // 5
        print(count) # 값을 출력하고
        break # break
    
    # 아니라면 설탕에서 3kg을 빼며, 주머니 수 +1
    sugar -= 3
    count += 1

else:
    # while-else, 설탕이 5x+3y로 구성되지 않은 경우 음수 출력
    print(-1)

    
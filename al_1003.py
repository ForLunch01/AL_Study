import sys

TC = int(sys.stdin.readline())
pList = []
maxNum = 0

for _ in range(TC):
    num = int(sys.stdin.readline())
    maxNum = max(maxNum, num)
    pList.append(num)

DP = [[0,0] for _ in range(41)] # 이걸로 하면 정답입니다.


DP[0] = [1, 0]
DP[1] = [0, 1]

if maxNum>1:
    for idx in range(2, maxNum+1):
        DP[idx][0] = DP[idx-1][0] + DP[idx-2][0]
        DP[idx][1] = DP[idx-1][1] + DP[idx-2][1]

for num in pList:
    print(*DP[num])
# 문제 정리
# 1번부터 N번까지 N명의 사람이 '원'을 이루며 앉음
# 양의 정수 K(<=N)가 주어짐
# 순서대로 K번째 사람을 제거한다
# N명의 사람이 모두 제거될 때까지 계속
# 원에서 사람들이 제거되는 순서를 N, K 요세푸스 순열이라고 함

# 풀이
# deque 사용.
# k번 rotate
# popleft()
# 그리고 그 값을 기록
# deque가 false가 될 때까지

from collections import deque

N, K = map(int, input().split())

# 크기 N, 오름차 순 인덱스를 가지는 deque 초기화
data = deque([i for i in range(1, N+1)])
yosep_list = []

while data:
    data.rotate(1-K)
    print(data)
    yosep_list.append(data.popleft())

print("<"+", ".join(map(str, yosep_list))+">")
    
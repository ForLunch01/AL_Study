# 조합을 이용한 코드
# 1. 1자리 부터 10자리 까지 0~9 까지 숫자의 조합을 구한다.

# 2. 순열이 아니라 조합이므로 중복되는 숫자는 등장하지 않는다.

# 3. 추출된 숫자를 거꾸로 정렬한다. 이후에 정답 배열에 넣어주면 끝이다

from itertools import combinations
import sys
input = sys.stdin.readline

def BOJ1038() :
  N = int(input())
  answers = []

  for i in range(1, 11) :
    for comb in combinations(range(0, 10), i) :
      comb = list(comb)
      comb.sort(reverse=True)
      answers.append(int("".join(map(str, comb))))

  answers.sort()
  
  try :
    print(answers[N])
  except :
    print(-1)
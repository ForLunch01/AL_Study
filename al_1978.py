import sys

input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

count = 0
for n in N_list:
    if n != 1:
        count += is_prime(n)

print(count)
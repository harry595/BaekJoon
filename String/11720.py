# https://www.acmicpc.net/problem/11720

N = int(input())
M = int(input())
summ = 0
for _ in range(N):
    summ += M % 10
    M = M//10
print(summ)

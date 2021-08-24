# https://www.acmicpc.net/problem/1932 정수 삼각형 문제
import sys

input = sys.stdin.readline
N = int(input())
S, E = map(int, input().split())
dp = [(S, 0), (E, 1)]
answer = 0
for i in range(N-1):
    S, E = map(int, input().split())
    dp.append((E, i+2))
dp2 = dp.copy()
dp.sort(reverse=True)


def findindex(t):
    left = 1
    right = 1
    if dp2[t-1][0] == -1:
        for i in range(t-2, -1, -1):
            if dp2[i][0] != -1:
                left = dp2[i][0]
                break
    else:
        left = dp2[t-1][0]

    if dp2[t+1][0] == -1:
        for i in range(t+2, N+1):
            if dp2[i][0] != -1:
                right = dp2[i][0]
                break
    else:
        right = dp2[t+1][0]

    return right, left


for j in dp:
    if j[1] == 0 or j[1] == N:
        continue
    right, left = findindex(j[1])
    answer += left*right*j[0]
    print(j[0])
    dp2[j[1]] = (-1, dp2[j[1]][1])
    print(answer)

print(answer)

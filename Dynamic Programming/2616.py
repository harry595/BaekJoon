# https://www.acmicpc.net/problem/1912 연속합 문제
# SUM 리스트를 만들어서 최댓값 - 최솟값
import sys

input = sys.stdin.readline
N = int(input())
train = list(map(int, input().split()))
size = int(input())

S = [0]
for i in range(len(train)):
    S.append(S[i]+train[i])
DP = [[0]*(N+1) for _ in range(4)]

for i in range(1, 4):
    for j in range(i*size, N+1):
        if i == 1:
            DP[i][j] = max(DP[i][j-1], S[j]-S[j-size])
        else:
            DP[i][j] = max(DP[i][j-1], DP[i-1][j-size]+S[j]-S[j-size])
print(DP[3][N])

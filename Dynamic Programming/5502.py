# https://www.acmicpc.net/problem/1912 연속합 문제
# SUM 리스트를 만들어서 최댓값 - 최솟값
import sys

input = sys.stdin.readline
N = int(input())
M = list(input().rstrip())
ON = M[::-1]
DP = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if M[i-1] != ON[j-1]:
            DP[i][j] = max(DP[i][j-1], DP[i-1][j])
        else:
            DP[i][j] = DP[i-1][j-1] + 1
print(N-DP[-1][-1])

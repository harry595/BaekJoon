# https://www.acmicpc.net/problem/1932 정수 삼각형 문제
# 전의 집과 겹치면 안되는 것만 확인
# 2차원 배열 형식으로 모든 집들에 전 집들의 cost를 추가하여 계산
import sys
input = sys.stdin.readline
N = int(input())
Narray = list(map(int, input().split()))
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(0, N+1):
    for start in range(1, N+1):
        end = start+i
        if end > N:
            break
        if i == 0:
            dp[start][end] = 1
            continue
        if i == 1 and Narray[start-1] == Narray[end-1]:
            dp[start][end] = 1
            continue
        if dp[start+1][end-1] and Narray[start-1] == Narray[end-1]:
            dp[start][end] = 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E])

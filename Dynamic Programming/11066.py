# https://www.acmicpc.net/problem/11053 가장 긴 증가하는 부분 수열 문제
# DP 리스트를 만들어서 해결
import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    result = 0
    tmp = int(input())
    T = list(map(int, input().split()))
    dp = [0 for _ in range(tmp+1)]
    dp[0] = T[0]
    dp[1] = T[0]+T[1]
    for i in range(2, tmp):
        dp[i] = min(dp[i-1]+T[i], dp[i-2]+T[i-1]+T[i])
    print(dp)

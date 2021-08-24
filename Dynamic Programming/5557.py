# https://www.acmicpc.net/problem/1516 게임 개발 문제

t = int(input())
gd = list(map(int, input().split()))
dp = [[0]*21 for _ in range(t)]

answer = gd.pop()
dp[0][gd[0]] = 1

for i in range(1, t-1):
    for j in range(21):
        if dp[i-1][j]:
            if j-gd[i] >= 0:
                dp[i][j-gd[i]] += dp[i-1][j]
            if j+gd[i] <= 20:
                dp[i][j+gd[i]] += dp[i-1][j]

print(dp[t-2][answer])

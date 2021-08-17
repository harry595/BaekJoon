# https://www.acmicpc.net/problem/2293

N, target = map(int, input().split())
Clist = []
for _ in range(N):
    Clist.append(int(input()))
dp = [0 for _ in range(target+1)]
dp[0] = 1
for c in Clist:
    for k in range(1, target+1):
        if k-c >= 0:
            dp[k] += dp[k-c]
print(dp[target])

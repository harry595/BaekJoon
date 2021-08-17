# https://www.acmicpc.net/problem/9084

T = int(input())
for i in range(T):
    N = int(input())
    Clist = list(map(int, input().split()))
    target = int(input())
    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    for c in Clist:
        for k in range(1, target+1):
            if k-c >= 0:
                dp[k] += dp[k-c]
    print(dp[target])

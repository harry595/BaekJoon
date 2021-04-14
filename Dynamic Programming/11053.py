# https://www.acmicpc.net/problem/11053 가장 긴 증가하는 부분 수열 문제
# DP 리스트를 만들어서 해결

N = int(input())
cost=list(map(int, input().split()))
dp=[ 1 for _ in range(N)]

for i in range(1,N):
    for j in range(0,i):
        if(cost[j]<cost[i]):
            if(dp[j]>=dp[i]):
                dp[i]=dp[j]+1
print(max(dp))
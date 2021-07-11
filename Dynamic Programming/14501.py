# https://www.acmicpc.net/problem/14501 퇴사
# DP 리스트를 만들어서 해결

N = int(input())
costs=[]
dp=[0]*(N+1)
for _ in range(N):
    costs.append(list(map(int, input().split())))
costs.append([0,0])
for i in range(N+1):
    date=costs[i][0]
    cash=costs[i][1]
    for j in range(i+date,N+1):
        if(dp[j] < cash+dp[i]):
            dp[j] = cash+dp[i]
print(dp[-1])
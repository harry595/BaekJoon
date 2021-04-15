# https://www.acmicpc.net/problem/1912 연속합 문제
# SUM 리스트를 만들어서 최댓값 - 최솟값

N = int(input())
cost=list(map(int, input().split()))
dp=[]
dp.append(cost[0])
if N==1:
    print(cost[0])
else:
    for i in range(1,N):
        dp.append(max(dp[i-1]+cost[i],cost[i]))
    print(max(dp))

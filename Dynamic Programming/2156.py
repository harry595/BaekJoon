# https://www.acmicpc.net/problem/2156 포도주 시식 문제
# 2579와 같지만 마지막 거를 고르지 않아도 되는게 다름

N = int(input())
cost= []
dp = [0 for i in range(N)]
for _ in range(N):
    cost.append(int(input()))
if(N==1):
    print(cost[0])
elif(N==2):
    print(cost[0]+cost[1])
elif(N==3):
    print(max(cost[0]+cost[2],cost[1]+cost[2],cost[0]+cost[1]))
else:
    dp[0]=cost[0]
    dp[1]=cost[0]+cost[1]
    dp[2]=max(cost[0]+cost[2],cost[1]+cost[2],cost[0]+cost[1])
    for i in range(3,N):
        dp[i]=max(dp[i-1],dp[i-3]+cost[i]+cost[i-1],dp[i-2]+cost[i])
    print(dp[N-1])
 
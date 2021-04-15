# https://www.acmicpc.net/problem/2579 계단 오르기 문제
# 두집씩 고르돼 다다음의 val이 전 두개보다 크면 다다음 val 선택하기

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
    print(max(cost[0]+cost[2],cost[1]+cost[2]))
else:
    dp[0]=cost[0]
    dp[1]=cost[0]+cost[1]
    dp[2]=max(cost[0]+cost[2],cost[1]+cost[2])
    for i in range(3,N):
        dp[i]=max(dp[i-3]+cost[i]+cost[i-1],dp[i-2]+cost[i])
    print(dp[N-1])

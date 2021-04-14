# https://www.acmicpc.net/problem/1149 RGB거리 문제
# 전의 집과 겹치면 안되는 것만 확인
# 2차원 배열 형식으로 모든 집들에 전 집들의 cost를 추가하여 계산

N = int(input())
cost= []
for _ in range(N):
    cost.append(list(map(int, input().split())))
for i in range(1,len(cost)):
    cost[i][0]=min(cost[i-1][1],cost[i-1][2])+cost[i][0]
    cost[i][1]=min(cost[i-1][0],cost[i-1][2])+cost[i][1]
    cost[i][2]=min(cost[i-1][0],cost[i-1][1])+cost[i][2]
print(min(cost[N-1][0],cost[N-1][1],cost[N-1][2]))

# https://www.acmicpc.net/problem/1932 정수 삼각형 문제
# 전의 집과 겹치면 안되는 것만 확인
# 2차원 배열 형식으로 모든 집들에 전 집들의 cost를 추가하여 계산

N = int(input())
cost= []
dp = [0 for i in range(501)]
for _ in range(N):
    cost.append(list(map(int, input().split())))

for i in range(1,N):
    for j in range(1,i):
        cost[i][j]=max(cost[i-1][j-1],cost[i-1][j])+cost[i][j]
    cost[i][0]=cost[i-1][0]+cost[i][0]
    cost[i][i]=cost[i-1][i-1]+cost[i][i]
print(max(cost[N-1]))

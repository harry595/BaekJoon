# https://www.acmicpc.net/problem/2056

T = int(input())
Clist = {}
cost = {0: 0}
for i in range(1, T+1):
    tmp = list(map(int, input().split()))
    cost[i] = tmp[0]
    if(len(tmp) == 2):
        Clist[i] = [0]
    else:
        Clist[i] = tmp[2:]

for j in range(1, T+1):
    temp = 0
    for k in Clist[j]:
        temp = max(temp, cost[k])
    cost[j] += temp
print(max(cost.values()))

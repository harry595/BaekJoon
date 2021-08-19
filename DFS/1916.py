# https://www.acmicpc.net/problem/1916


def DFS(start, end, cost):
    global answer
    if start == end:
        if cost < answer:
            answer = cost
    for i in range(1, M+1):
        if Mgraph[start][i] != 0:
            cost += Mgraph[start][i]
            if answer <= cost:
                pass
            DFS(i, end, cost)
            cost -= Mgraph[start][i]


answer = 100000000
N = int(input())
M = int(input())
Mgraph = [[0 for _ in range(M+1)] for _ in range(M+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    Mgraph[a][b] = c
start, end = map(int, input().split())
DFS(start, end, 0)
print(answer)

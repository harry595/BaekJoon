# https://www.acmicpc.net/problem/2606 바이러스 문제 DFS

from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**9)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
input = stdin.readline
answer = 0


def DFS(i, j):
    if visit[i][j] < 0:
        visit[i][j] = 0
        for k in range(4):
            xindex = i+dx[k]
            yindex = j+dy[k]
            if 0 <= xindex < N and 0 <= yindex < N and Pgraph[i][j] < Pgraph[xindex][yindex]:
                visit[i][j] = max(visit[i][j], DFS(xindex, yindex))
        visit[i][j] += 1
    return visit[i][j]


N = int(input())
Pgraph = []
visit = [[-1] * N for i in range(N)]

for _ in range(N):
    Pgraph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        answer = max(DFS(i, j), answer)

print(answer)

# https://www.acmicpc.net/problem/2606 바이러스 문제 DFS

from sys import stdin

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
input = stdin.readline
answer = 0


def DFS(i, j):
    global answer
    for k in range(4):
        xindex = i+dx[k]
        yindex = j+dy[k]
        if 0 <= xindex < R and 0 <= yindex < C and not Pgraph[xindex][yindex] in Pqueue:
            Pqueue.append(Pgraph[xindex][yindex])
            answer = max(len(Pqueue), DFS(xindex, yindex))
            Pqueue.pop()
    return answer


R, C = map(int, input().split())
Pgraph = []
visit = [[0] * C for i in range(R)]
for _ in range(R):
    Pgraph.append(list(input().rstrip()))

Pqueue = [Pgraph[0][0]]
print(DFS(0, 0))

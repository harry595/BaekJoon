# https://www.acmicpc.net/problem/1916
import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N = int(input())
M = int(input())

Mgraph = [[] for _ in range(N+1)]
distance = [sys.maxsize]*(N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    Mgraph[a].append([b, c])
start, end = map(int, input().split())


def dijkstra(start):
    heap = []
    heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        cost, index = heappop(heap)
        if distance[index] < cost:
            continue
        for a, b in Mgraph[index]:
            if cost+b < distance[a]:
                distance[a] = cost+b
                heappush(heap, (cost+b, a))


dijkstra(start)
print(distance[end])

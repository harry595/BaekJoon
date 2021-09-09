# https://www.acmicpc.net/problem/51202
import sys
import heapq
input = sys.stdin.readline

Nlists = []
Klists = []
N, K = map(int, input().split())

for _ in range(N):
    a, b = map(int, input().split())
    Nlists.append([a, b])

for _ in range(K):
    c = int(input())
    Klists.append(c)

Nlists.sort()
Klists.sort()

result = 0
tmp = []
for Klist in Klists:
    while Nlists and Klist >= Nlists[0][0]:
        heapq.heappush(tmp, -Nlists[0][1])
        heapq.heappop(Nlists)
    if tmp:
        result += heapq.heappop(tmp)
    elif not Nlists:
        break
print(-result)

# https://www.acmicpc.net/problem/2606 바이러스 문제 BFS
from sys import stdin
from collections import deque

def BFS(graph):
    queue = deque([1])
    visited = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited

def _2606():
    answer = 0
    n = int(stdin.readline())
    m = int(stdin.readline())
    graph = [set() for _ in range(n+1)]
    for _ in range(m):
        src, dest = map(int, stdin.readline().split())
        graph[src].add(dest)
        graph[dest].add(src)
    print(graph)
    result = BFS(graph)
    print(len(result)-1)

_2606()
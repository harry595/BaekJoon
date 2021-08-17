# https://www.acmicpc.net/problem/2056

N, M = map(int, input().split())
indegree = [0 for i in range(N+1)]
Tlist = [[] for i in range(N+1)]
queue = []
answer = []
for _ in range(M):
    a, b = map(int, input().split())
    Tlist[a].append(b)
    indegree[b] += 1

for j in range(1, N+1):
    if indegree[j] == 0:
        queue.append(j)

while(queue):
    for i in queue:
        answer.append(i)
        queue.remove(i)
        for t in Tlist[i]:
            indegree[t] -= 1
            if(indegree[t] == 0):
                queue.append(t)

for ans in answer:
    print(ans, end=" ")

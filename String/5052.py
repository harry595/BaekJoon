# https://www.acmicpc.net/problem/5052
from sys import stdin
input = stdin.readline

N = int(input())
for _ in range(N):
    answerflag = True
    M = int(input())
    nlist = []
    for j in range(M):
        nlist.append(input().strip())
    nlist.sort()
    for k in range(len(nlist)-1):
        if nlist[k] in nlist[k+1][0:len(nlist[k])]:
            print('NO')
            answerflag = False
            break
        else:
            continue
    if answerflag:
        print('YES')

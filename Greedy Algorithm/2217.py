# https://www.acmicpc.net/problem/2217 로프 문제

from sys import stdin

t=int(stdin.readline())
gd=[]
result=[]
for _ in range(t):
    gd.append(int(stdin.readline()))
gd.sort(reverse=True)
for i in range(0,t):
    result.append(gd[i]*(i+1))
print(max(result))


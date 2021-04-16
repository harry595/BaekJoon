# https://www.acmicpc.net/problem/1931 회의실 배정 문제

N = int(input())
RESULT=0
gd = []
for i in range(N):
    first, second = map(int, input().split())
    gd.append([first, second])
gd = sorted(gd, key=lambda x: (x[1],x[0]))
last=0
for j,k in gd:
    if(j>=last):
        RESULT+=1
        last=k
print(RESULT)
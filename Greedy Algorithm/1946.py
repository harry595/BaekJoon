# https://www.acmicpc.net/problem/1946 신입사원 문제

from sys import stdin

t=int(input())
for _ in range(t):
    cnt=1
    gd=[]
    num=int(input())  

    for _ in range(num):
        gd.append(list(map(int, stdin.readline().split())))
    gd = sorted(gd, key=lambda x: (x[0]))
    min_rank=gd[0][1]
    for i in range(1,num):
        if(gd[i][1] < min_rank):
            min_rank=gd[i][1]
            cnt+=1
    print(cnt)


# https://www.acmicpc.net/problem/1912 연속합 문제
# SUM 리스트를 만들어서 최댓값 - 최솟값
from datetime import datetime, timedelta
from sys import stdin
input = stdin.readline

N = int(input())
result=[]
cost=[]
for i in range(N):
    num,time=map(int, input().split())
    date_list=[]
    
    for j in range(num):
        at,bt,ct,dt,et=input().split()
        y,m,d=map(int, bt.split('-'))
        h,mn=map(int, ct.split(':'))
        sdate = datetime(y, m, d, h, mn)
        y,m,d=map(int, dt.split('-'))
        h,mn=map(int, et.split(':'))
        edate = datetime(y, m, d, h, mn)+timedelta(minutes=time)
        date_list.append((sdate,1))
        date_list.append((edate,-1))

    date_list.sort()
    res=0
    cur=0
    for st,en in date_list:
        cur+=en
        res=max(res,cur)

    print(res)
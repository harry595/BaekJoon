# https://www.acmicpc.net/problem/5585 거스름돈 문제

N = 1000-int(input())
money=[500,100,50,10,5,1]
answer=0
for i in money:
    answer+=N//i
    N=N%i
print(answer)
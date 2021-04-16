# https://www.acmicpc.net/problem/10162 전자레인지 문제

N = int(input())
cost=[300,60,10]
answer=[]
for i in cost:
    answer.append(N//i)
    N=N%i
    
if N!= 0:
    print(-1)
else:
    for i in answer:
        print(i,end=" ")
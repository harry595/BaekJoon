# https://www.acmicpc.net/problem/2577 숫자의 개수 문제

A = int(input())
B = int(input())
C = int(input())
mul=A*B*C
result=[0 for _ in range(10)]
for i in str(mul):
    tmp=int(i)
    result[tmp]+=1

for j in result:
    print(j)
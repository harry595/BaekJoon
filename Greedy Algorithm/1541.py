# https://www.acmicpc.net/problem/1541 잃어버린 괄호 문제


N = input().split('-')
M=N[0].split('+')
RESULT=0
for i in M:
    RESULT+=int(i)
for i in N[1:]:
    for j in i.split('+'):
        RESULT-=int(j)
print(RESULT)

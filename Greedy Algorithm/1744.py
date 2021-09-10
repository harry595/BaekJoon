# https://www.acmicpc.net/problem/1946 신입사원 문제

from sys import stdin
input = stdin.readline

t = int(input())
minus = 0
oneval = 0
gd = []
for _ in range(t):
    tmp = int(input())
    if tmp <= 0:
        minus += 1
    elif tmp == 1:
        oneval += 1
    gd.append(tmp)

gd.sort()
minusgd = gd[:minus]
plusgd = gd[minus+oneval:][::-1]
answer = 0

for a, i in enumerate(minusgd[::2]):
    try:
        answer += i*minusgd[2*a+1]
    except:
        answer += i

for a, i in enumerate(plusgd[::2]):
    try:
        answer += i*plusgd[2*a+1]
    except:
        answer += i

print(answer+oneval)

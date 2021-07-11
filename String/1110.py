# https://www.acmicpc.net/problem/1110 더하기 사이클 문제


N = int(input())
N2=N
result=0
while True:
    left=N2//10
    right=N2%10
    realright=(left+right)%10
    N2=right*10+realright
    result+=1
    if(N2==N):
        print(result)
        break
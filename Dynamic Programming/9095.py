# https://www.acmicpc.net/problem/9095 1,2,3 더하기 문제 
# 점화식 사용
from sys import stdin

def sol(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    return sol(n-1)+sol(n-2)+sol(n-3)
if __name__ == "__main__":
    t=int(stdin.readline())
    print(sol(int(stdin.readline())))
    

            

            

    
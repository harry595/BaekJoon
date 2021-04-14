# https://www.acmicpc.net/problem/1003 피보나치 함수 문제
# fib(0)= fib(0)  1 0
# fib(1)= fib(1)  0 1
# fib(2)= fib(1) + fib(0)  1 1
# fib(3)= fib(2) + fib(1) = fib(1) + fib(0) + fib(1)  1 2
# fib(4)= fib(3) + fib(2) = fib(1) + fib(0) + fib(1) + fib(1) + fib(0) 2 3
# fib랑 똑같이 0 일때 1일때가 전꺼 두개 합한거랑 같음
from sys import stdin

zero_arr=[1,0,1]
one_arr=[0,1,1]
def sol(n):
    length=len(zero_arr)
    if (length<=n):
        for i in range(length,n+1):
                zero_arr.append(zero_arr[i-1]+zero_arr[i-2])
                one_arr.append(one_arr[i-1]+one_arr[i-2])
    print(zero_arr[n],one_arr[n])
if __name__ == "__main__":
    t=int(stdin.readline())
    for _ in range(t):
        tmp=int(stdin.readline())
        sol(tmp)

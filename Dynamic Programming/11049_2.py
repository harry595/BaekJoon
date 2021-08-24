# https://www.acmicpc.net/problem/1932 정수 삼각형 문제
import sys
import numpy

input = sys.stdin.readline
N = int(input())
S, E = map(int, input().split())
dp = [[S, S], [E, E]]
answer = 0
for i in range(N-1):
    S, E = map(int, input().split())
    dp.append([E, E])

for i in range(1, N):
    dp[i][0] = dp[i-1][1]*dp[i+1][1]*dp[i][0]

end = dp.pop()[0]
start = dp.pop(0)[0]

while len(dp) != 1:
    minval = list(numpy.argmin(dp, axis=0))[0]
    answer += dp[minval][0]
    if minval == 0:
        pass
    elif minval == len(dp)-1:
        dp[minval-1][0] = dp[minval-1][0]//dp[minval][1]*end
    else:
        dp[minval-1][0] = dp[minval-1][0]//dp[minval][1]*dp[minval+1][1]

    if minval == len(dp)-1:
        pass
    elif minval == 0:
        dp[minval+1][0] = dp[minval+1][0]//dp[minval][1]*start
    else:
        dp[minval+1][0] = dp[minval+1][0]//dp[minval][1]*dp[minval-1][1]
    dp.pop(minval)

print(answer+dp[0][0])

# https://www.acmicpc.net/problem/9461 파도반 수열

N = int(input())
inp=[]
for _ in range(N):
   inp.append(int(input()))

dp=[1,1,1,2,2,3,4,5,7]
for i in range(9,101):
    dp.append(dp[i-3]+dp[i-2])

for j in inp:
    print(dp[j-1])


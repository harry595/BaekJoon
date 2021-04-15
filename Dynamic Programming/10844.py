# https://www.acmicpc.net/problem/10844 쉬운 계단 수 문제
#

N = int(input())
dp_before=[0,1,1,1,1,1,1,1,1,1]
dp_after=dp_before[:]

if N==1:
    print(sum(dp_before))
else:
    for i in range(1,N):
        dp_before=dp_after[:]
        for j in range(1,9):
            dp_after[j]=dp_before[j-1]+dp_before[j+1]
        dp_after[0]=dp_before[1]
        dp_after[9]=dp_before[8]
    print(sum(dp_after)%1000000000)
# https://www.acmicpc.net/problem/11057

N = int(input())
dp=[1,1,1,1,1,1,1,1,1,1]
tmpdp=[0,0,0,0,0,0,0,0,0,0]
if(N==1):
    print(10)
else:
    for i in range(N-1):
        sumdp=sum(dp)
        tmpdp[0]=sumdp
        tmpdp[1]=tmpdp[0]-dp[0]
        tmpdp[2]=tmpdp[1]-dp[1]
        tmpdp[3]=tmpdp[2]-dp[2]
        tmpdp[4]=tmpdp[3]-dp[3]
        tmpdp[5]=tmpdp[4]-dp[4]
        tmpdp[6]=tmpdp[5]-dp[5]
        tmpdp[7]=tmpdp[6]-dp[6]
        tmpdp[8]=tmpdp[7]-dp[7]
        tmpdp[9]=tmpdp[8]-dp[8]
        dp=tmpdp.copy()
    print(sum(dp)%10007)


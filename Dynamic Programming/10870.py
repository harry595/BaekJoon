# https://www.acmicpc.net/problem/10870 피보나치 수 5  문제


t=int(input())
if(t==0):
    print(0)
elif(t==1):
    print(1)
elif(t==2):
    print(1)
else:
    tmp_arr=[0,1,1]
    for i in range(3,t+1):
        tmp_arr.append(tmp_arr[i-2]+tmp_arr[i-1])
    print(tmp_arr[t])
# https://www.acmicpc.net/problem/11727 2×n 타일링 2 문제
# sol(1)=1 sol(2)=3 sol(3)=5 
def sol(n):
    tmp_arr=[0,1,3]
    for i in range(3,n+1):
        tmp_arr.append(tmp_arr[i-2]*2+tmp_arr[i-1])
    print(tmp_arr[n]%10007)
if __name__ == "__main__":
    t=int(input())
    if(t==1):
        print(1)
    elif(t==2):
        print(3)
    else:
        sol(t)
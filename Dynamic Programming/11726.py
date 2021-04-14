# https://www.acmicpc.net/problem/11726 2×n 타일링 문제
# sol(1)=1 sol(2)=2 sol(3)=3 sol(4)=5
def sol(n):
    tmp_arr=[0,1,2]
    for i in range(3,n+1):
        tmp_arr.append(tmp_arr[i-2]+tmp_arr[i-1])
    print(tmp_arr[n]%10007)
if __name__ == "__main__":
    t=int(input())
    sol(t)
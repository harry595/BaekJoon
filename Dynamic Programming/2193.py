# https://www.acmicpc.net/problem/2193 이친수 문제
# sol(1)=1 sol(2)=2 sol(3)=3 sol(4)=5
RESULT=0

def sol(result_list,i,t):
    tmp_list1=result_list[:]
    if(i==t):
        global RESULT
        RESULT+=1
        return
    if(tmp_list1[i-1]==1):
        tmp_list1.append(0)
        return sol(tmp_list1,i+1,t)
    else:
        tmp_list=tmp_list1[:]
        tmp_list.append(1)
        tmp_list1.append(0)
        return sol(tmp_list1,i+1,t),sol(tmp_list,i+1,t)
if __name__ == "__main__":
    t=int(input())
    result_list=[1]
    sol(result_list,1,t)
    print(RESULT)
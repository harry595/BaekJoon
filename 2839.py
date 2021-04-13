# https://www.acmicpc.net/problem/2839 설탕배달 문제
# 3,6,9,12,15,18,21,24,27,30 이런식 (1,2,3,4,5,6,7,8,9 모두 가능)
# 5,10,15,20
# 우선 30이 넘을 경우 5Xt 로 남기고 연산 수행

def sol():
    input_val=int(input())
    if (input_val >= 30):
        thirty=(input_val-30)%5
        result_five=(input_val-30)//5
        thirty=thirty+30
        for i in reversed(range(9)):
            if(i*5>thirty):
                pass
            elif( (thirty-i*5)%3==0 ):
                result_three=(thirty-i*5)//3
                return(result_three+i+result_five)
    else:
        for i in reversed(range(7)):
            if(i*5>input_val):
                pass
            elif( (input_val-i*5)%3==0 ):
                result_three=(input_val-i*5)//3
                return(result_three+i)
    return(-1)
if __name__ == "__main__":
    print(sol())
    

            

            

    
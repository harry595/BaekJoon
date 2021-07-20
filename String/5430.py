# https://www.acmicpc.net/problem/5430


import json
answer=[]
N = int(input())
for i in range(N):
    rd=input()
    count=int(input())
    arr=input()
    arr=json.loads(arr)
    rcount=0
    errflag=0
    for j in rd:
        if j =='R':
            rcount+=1
        else:
            try:
                if rcount % 2 == 1:
                    del(arr[-1])
                else:
                    del(arr[0])
            except:
                errflag=1
                answer.append('error')
                break
    if errflag==0:
        if rcount % 2 == 1:
            answer.append(arr[::-1])
        else:
            answer.append(arr)
    else:
        errflag=0
for i in answer:
    print(str(i).replace(' ',''))
    
'''

for i in range(int(input())):
    q = input()
    arr_len = int(input())
    if(arr_len == 0):
        input_arr = input()
        input_arr = []
    else:
        input_arr = list(map(int, input()[1:-1].split(',')))
    is_reverse = False
    is_ok = True
    front = 0
    rear = 0
    
    for act in q:
        try:
            if(act == 'R'):
                is_reverse = not is_reverse
            elif(act == 'D' and not is_reverse):
                front += 1
            elif(act == 'D' and is_reverse):
                rear += 1
        except:
            is_ok = False
            print('error')
            break

    if(is_ok):
        if(front + rear <= arr_len):
            if(not is_reverse):
                input_arr = input_arr[front:arr_len - rear]
                print(str(input_arr).replace(' ', ''))
            else:
                input_arr = input_arr[::-1][rear:arr_len - front]
                print(str(input_arr).replace(' ', ''))
        else:
            print('error')
'''
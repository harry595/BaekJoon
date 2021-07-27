# https://www.acmicpc.net/problem/5430


import json
answer = []
N = int(input())
for i in range(N):
    rd = input()
    count = int(input())
    arr = input()
    arr = json.loads(arr)
    rcount = 0
    errflag = 0
    for j in rd:
        if j == 'R':
            rcount += 1
        else:
            try:
                if rcount % 2 == 1:
                    del(arr[-1])
                else:
                    del(arr[0])
            except:
                errflag = 1
                answer.append('error')
                break
    if errflag == 0:
        if rcount % 2 == 1:
            answer.append(arr[::-1])
        else:
            answer.append(arr)
    else:
        errflag = 0
for i in answer:
    print(str(i).replace(' ', ''))

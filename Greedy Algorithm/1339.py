# https://www.acmicpc.net/problem/1339 단어 수학 문제

from sys import stdin

t=int(input())
dic={}
for _ in range(t):
    gd=[]
    gd.append(list(map(str, stdin.readline().split())))
    for i in range(len(gd)):
        for cnt,j in enumerate(gd[i][0]):
            if( j not in dic.keys()):
                dic[j]=10**(len(gd[i][0])-cnt-1)
            else:
                dic[j]+=10**(len(gd[i][0])-cnt-1)

dic = sorted(dic.items(), key=(lambda x: x[1]), reverse = True)
result=0
for i in range(len(dic)):
    result+=dic[i][1]*(9-i)
print(result)


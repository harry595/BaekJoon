# https://www.acmicpc.net/problem/1516 게임 개발 문제

from sys import stdin

t=int(input())
dic={}
gd=[[0]]
for _ in range(t):
    gd.append(list(map(int, stdin.readline().split())))
build_list={}
del_list=[]
while(len(del_list)!=t):
    lengd=len(gd)
    for i in range(1,lengd):
        if i in del_list:
            pass
        else:
            if( len(gd[i]) == 2):
                build_list[i]=gd[i][0]
                del_list.append(i)
            elif( set(gd[i][1:-1]).issubset(set(build_list.keys()))):
                tmp_list=[]
                for tmp in gd[i][1:-1]: 
                    tmp_list.append(build_list[tmp])
                build_list[i]=max(tmp_list)+gd[i][0]
                del_list.append(i)
build_list = sorted(build_list.items(), key=(lambda x: x[0]))
for i in build_list:
    print(i[1])

            
        
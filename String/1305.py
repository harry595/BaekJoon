# https://www.acmicpc.net/problem/1305 

N = int(input())
ads=input()
answer=[ads[0]]
ancount=0
lenan=1
for i,ad in enumerate(ads):
    print(lenan)
    if ad == ads[ancount]:
        ancount+=1
        ancount=ancount%lenan
    else:
        ancount=0
        lenan=i+1
print(lenan)

# https://www.acmicpc.net/problem/5052
import sys
input = sys.stdin.readline
N = input()
liquid = list(map(int, input().split()))

liquid.sort()
reverseli = liquid[::-1]
answer = 2100000000
start = 0
end = 0
for i in liquid:
    tmp = 2100000000
    a, b = 0, 2100000000
    if i > 0:
        break
    for j in reverseli:
        if j > b:
            continue
        if j < 0:
            break
        absij = abs(i+j)
        if absij < tmp:
            tmp = absij
            a, b = i, j
        else:
            if tmp < answer:
                answer = tmp
                start = a
                end = b
            break

print(str(start), str(end))

# https://www.acmicpc.net/problem/15649
from itertools import combinations

while True:
    A = list(map(int, input().split()))[1:]
    if not A:
        break
    permute = combinations(A, 6)
    for perm in list(permute):
        for per in perm:
            print(per, end=' ')
        print()
    print()

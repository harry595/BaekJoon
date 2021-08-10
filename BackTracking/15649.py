# https://www.acmicpc.net/problem/15649
from itertools import permutations

A, B = map(int, input().split())

numlist = [tmp for tmp in range(1, A+1)]
permute = permutations(numlist, B)
for perm in list(permute):
    for per in perm:
        print(per, end=' ')
    print()

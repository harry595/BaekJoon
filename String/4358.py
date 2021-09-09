# https://www.acmicpc.net/problem/5052
import sys
from typing import DefaultDict
input = sys.stdin.readline

n = 0
trees = DefaultDict(int)
while True:
    a = input().rstrip()
    if not a:
        break
    trees[a] += 1
    n += 1

trees2 = list(trees.keys())
trees2.sort()
for a in trees2:
    print('%s %.4f' % (a, trees[a]/n*100))

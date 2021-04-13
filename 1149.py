# https://www.acmicpc.net/problem/11726 2×n 타일링 문제
# sol(1)=1 sol(2)=2 sol(3)=3 sol(4)=5

N = int(input())
cost_per_home = []
for _ in range(N):
    cost_per_home.append(list(map(int, input().split())))
    
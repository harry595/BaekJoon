# https://www.acmicpc.net/problem/1915
# SUM 리스트를 만들어서 최댓값 - 최솟값

case = []
N, M = map(int, input().split())
for _ in range(N):
    case.append(list(map(int, input().rstrip())))
answer = 0

for i in range(0, N):
    for j in range(0, M):
        if i > 0 and j > 0 and case[i][j] != 0:
            case[i][j] += min(case[i-1][j-1], case[i][j-1], case[i-1][j])
        answer = max(answer, case[i][j])

print(answer*answer)

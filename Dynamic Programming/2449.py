# https://www.acmicpc.net/problem/1912 연속합 문제
# SUM 리스트를 만들어서 최댓값 - 최솟값

N, K = map(int, input().split())
light = list(map(int, input().split()))
dp = [light[0]]

for i in range(1, N):
    if light[i-1] != light[i]:
        dp.append(light[i])
print(dp)

for j in range(0, len(dp)):
    print(j)

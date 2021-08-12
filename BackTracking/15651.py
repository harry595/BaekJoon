# https://www.acmicpc.net/problem/15649
A, B = map(int, input().split())
visit = [False]*A
result = []


def backtracking(depth, A, B):
    if depth == B:
        print(' '.join(map(str, result)))
        return
    for i in range(A):
        result.append(i+1)
        backtracking(depth+1, A, B)
        result.pop()


backtracking(0, A, B)

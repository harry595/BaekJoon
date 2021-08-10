# https://www.acmicpc.net/problem/15649
A, B = map(int, input().split())
visit = [False]*A
result = []


def backtracking(depth, A, B):
    if depth == B and result == sorted(result):
        print(' '.join(map(str, result)))
        return
    for i in range(A):
        if not visit[i]:
            visit[i] = True
            result.append(i+1)
            backtracking(depth+1, A, B)
            visit[i] = False
            result.pop()


backtracking(0, A, B)

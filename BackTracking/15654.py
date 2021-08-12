# https://www.acmicpc.net/problem/15649
A, B = map(int, input().split())
C = list(map(int, input().split()))
C.sort()
result = []
visit = [False]*A


def backtracking(depth, A, B):
    if depth == B:
        print(' '.join(map(str, result)))
        return
    for i in range(A):
        if visit[i] == True:
            continue
        if len(result) > 0:
            if result[-1] > C[i]:
                continue
        visit[i] = True
        result.append(C[i])
        backtracking(depth+1, A, B)
        result.pop()
        visit[i] = False


backtracking(0, A, B)

# https://www.acmicpc.net/problem/15649
A, B = map(int, input().split())
result = []


def backtracking(depth, A, B):
    if depth == B:
        print(' '.join(map(str, result)))
        return
    for i in range(A):
        if len(result) == 0:
            pass
        elif result[-1] > i+1:
            continue
        result.append(i+1)
        backtracking(depth+1, A, B)
        result.pop()


backtracking(0, A, B)

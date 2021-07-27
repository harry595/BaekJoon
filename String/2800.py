# https://www.acmicpc.net/problem/2800

import itertools
ina = input()
count = 1
lenina = len(ina)
arrina = [0]*lenina
stacknum = []
stacknum2 = []
where = []
for i, arr in enumerate(ina):
    if arr == '(':
        arrina[i] = count
        stacknum.append(count)
        stacknum2.append(i)
        count += 1
    elif arr == ')':
        arrina[i] = stacknum.pop()
        where.insert(0, [i, stacknum2.pop()])
count -= 1

answer = []
case = []
for i in range(1, count+1):
    case.extend(list(itertools.combinations(where, i)))
for cas in case:
    tmpina = list(ina)
    for ca in cas:
        for c in ca:
            tmpina[c] = ' '
    answer.append(''.join(tmpina).replace(" ", ""))
answer = set(answer)
answer = list(answer)
for ai in sorted(answer):
    print(ai)
'''


from itertools import combinations
problem = [*input().strip()]
# 문자열 하나씩 리스트화
p, idx_brs = [], []  # 짝이 맞는 괄호의 위치 idx_brs에 저장해줌
for i, v in enumerate(problem):
    if v == '(':
        problem[i] = ''
        p += [i]
    if v == ')':
        problem[i] = ''
        idx_brs += [[p.pop(), i]]
out = set()
for i in range(len(idx_brs)):
    for j in combinations(idx_brs, i):
        print(j)
        P = problem[:]
        for v, w in j:
            P[v] = '('
            P[w] = ')'
        out.add(''.join(P))
for i in sorted(out):
    print(i)

'''

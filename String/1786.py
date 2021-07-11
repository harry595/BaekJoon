# https://www.acmicpc.net/problem/1786 찾기 문제 (KMP)

T = input()
P = input()

KMPTable = [0 for _ in range(len(P))]


def MakeTable(P, KMPTable):
    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = KMPTable[j-1]
        if P[i] == P[j]:
            j += 1
            KMPTable[i] = j


def KMP(T, P, KMPTable):
    MakeTable(P, KMPTable)
    j = 0
    count = 0
    result = []
    P_size = len(P)
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = KMPTable[j-1]
        if T[i] == P[j]:
            if j == P_size-1:
                count += 1
                result.append(i-P_size+2)
                j = KMPTable[j]
            else:
                j += 1
    return count, result


MakeTable(P, KMPTable)
count, result = KMP(T, P, KMPTable)
print(count)
for i in result:
    print(i, end=" ")

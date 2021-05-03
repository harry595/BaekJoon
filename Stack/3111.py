# https://www.acmicpc.net/problem/3111 검열 문제
# 문자열을 스택으로 넣으며 진행
import sys
sys.setrecursionlimit(10**6)

def first(ing_f,ing_l):
    if ing_f+ing_l == len(T):
        return

    while True:
        if( stack_front[-len(A):] == A[:]):
            del(stack_front[-len(A):])
            del(T[ing_f-len(A):ing_f])
            ing_f-=len(A)
            return last(ing_f,ing_l)
        else:
            stack_front.append(T[ing_f])
            ing_f+=1
            if ing_f+ing_l == len(T):
                return


def last(ing_f,ing_l):
    if ing_f+ing_l == len(T):
        return
    while True:
        if( stack_last[:len(A)] == A[:]):
            del(stack_last[:len(A)])
            if(ing_l==len(A)):
                del(T[-ing_l:])
            else:
                del(T[-ing_l:-ing_l+len(A)])
             
            ing_l-=len(A)
            return first(ing_f,ing_l)
        else:
            stack_last.insert(0,T[-ing_l-1])
            ing_l+=1
            if ing_f+ing_l == len(T):
                return


A=list(input())
T=list(input())
stack_front=T[:len(A)]
stack_last=T[-len(A):]
first(len(A),len(A))
print("".join(stack_front+stack_last))
# 1 4 7 9 11 -> 1 4 6 -> C(1~6) - C(1~3) - C(5~6)
import math


def comb(n, r):
    f = math.factorial
    return f(n)//f(r)//f(n-r)


def counting(a):
    first_index = a[0]  # 0
    second_index = a[1]  # 1
    last_index = a[-1]-a[-2]+second_index  # 2
    # [0~a~b~c] a에 배열을 주자
    # 1,2,3,4 -> k는 2,3
    return comb(first_index, last_index)-comb(first_index, second_index-1)-comb(second_index+1, last_index)


student = [0, 1, 0, 0, 1, 1, 0]
k = 2
oneindex = []
answer = 0
for count, i in enumerate(student):
    if i == 1:
        oneindex.append(count)
# k=1일떄를 고려
# 첫번째,마지막 case는 따로 고려
for i in range(len(oneindex)-k):
    a = oneindex[i:i+k]
    a[0] += 1
    a[-1] -= 1
    answer += counting(a)
answer = -1
print(answer)

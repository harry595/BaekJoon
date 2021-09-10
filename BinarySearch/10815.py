import sys

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

card.sort()


def binary_search(target):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2

        if card[mid] == target:
            return mid
        elif card[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if binary_search(check[i]) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')

# https://www.acmicpc.net/problem/6549 히스토그램에서 가장 큰 직사각형 문제
# (2,1) stack 넣고 만약 [0]이 현재 높이 보다 크면 pop()
while True:
    n, *heights = list(map(int, input().split()))
    if(n == 0):
        break
    
    heights.insert(0, 0)
    heights += [0]
    checked = [0]
    area = 0
    
    for i in range(1, n + 2):
        while(checked and (heights[checked[-1]] > heights[i])):
            cur_height = checked.pop()
            area = max(area, (i - 1 - checked[-1]) * heights[cur_height])
        checked.append(i)
    print(area)
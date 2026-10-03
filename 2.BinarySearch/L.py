def good(m):
    cnt = 0
    i = 0
    while i + C <= N:
        if heights[i + C - 1] - heights[i] <= m:
            cnt += 1
            i += C
        else:
            i += 1
    return cnt >= R

N, R, C = map(int, input().split())
heights = [int(input()) for i in range(N)]
heights.sort()

l = -1
r = heights[-1] - heights[0] + 1
while r - l > 1:
    m = (l + r) // 2
    if good(m):
        r = m
    else:
        l = m
print(r)
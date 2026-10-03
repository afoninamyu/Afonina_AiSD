def balloons(T, t, z, y):
    turn = t * z + y
    return T // turn * z + min(z, T % turn // t)

def good(T):
    res = 0
    for t, z, y in hlps:
        res += balloons(T, t, z, y)
    return res >= M

M, N = map(int, input().split())
hlps = [list(map(int, input().split())) for i in range(N)]

l = -1
r = 10**18
while r - l > 1:
    m = (l + r) // 2
    if good(m):
        r = m
    else:
        l = m
T = r
print(T)

ans = []
for t, z, y in hlps:
    blow = min(balloons(T, t, z, y), M)
    ans.append(blow)
    M -= blow
print(*ans)
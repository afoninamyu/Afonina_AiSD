A, K, B, M, X = map(int, input().split())
l = 0
r = 10**20
while r - l > 1:
    m = (l + r) // 2
    if A * (m - m // K) + B * (m - m // M) >= X:
        r = m
    else:
        l = m
print(r)
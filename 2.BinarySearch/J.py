def good(d, n, a, b, w, h):
    a_safe = a + 2 * d
    b_safe = b + 2 * d
    return (w // a_safe) * (h // b_safe) >= n or (h // a_safe) * (w // b_safe) >= n

n, a, b, w, h = map(int, input().split())
l = 0
r = 10**18
while r - l > 1:
    m = (l + r) // 2
    if good(m, n, a, b, w, h):
        l = m
    else:
        r = m
print(l)
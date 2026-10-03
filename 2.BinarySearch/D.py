def f(x):
    return a*x**3 + b*x**2 + c*x + d

a, b, c, d = map(int, input().split())

l, r = -10000.0, 10000.0
while r - l > 1e-5:
    m = (l + r) / 2
    if f(m) * a < 0:
        l = m
    else:
        r = m
print(m)
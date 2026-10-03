C = float(input())

l, r = 0.0, C
while r - l > 1e-7:
    m = (l + r) / 2
    if m**2 + m**0.5 < C:
        l = m
    else:
        r = m
print(f"{r:.9f}")
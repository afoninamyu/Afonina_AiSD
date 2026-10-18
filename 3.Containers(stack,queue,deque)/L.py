n, *h = map(int, input().split())
h += [0]
stack = []
ans = 0
for i in range(n+1):
    cur_h = h[i]
    lt = i
    while stack and stack[-1][1] >= cur_h:
        lt, prev_h = stack.pop()
        ans = max(ans, prev_h * (i - lt))
    if not stack or stack[-1][1] < cur_h:
        stack.append((lt, cur_h))
print(ans)
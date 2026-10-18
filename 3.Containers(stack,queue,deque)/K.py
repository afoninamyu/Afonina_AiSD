n = int(input())
d = list(map(int, input().split()))
stack = []

pr_sum = [0] * (n + 1)
for i in range(n):
    pr_sum[i + 1] = pr_sum[i] + d[i]

d += [0]
ans = 0
bl = 1
br = 1
for i in range(n + 1):
    cur_d = d[i]
    lt = i
    while stack and stack[-1][1] >= cur_d:
        lt, prev_d = stack.pop()
        res = prev_d * (pr_sum[i] - pr_sum[lt])
        if res > ans:
            ans = res
            bl, br = lt + 1, i
    if not stack or stack[-1][1] < cur_d:
        stack.append((lt, cur_d))
print(ans)
print(bl, br)
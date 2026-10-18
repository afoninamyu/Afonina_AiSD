from collections import deque
n = int(input())
lt = deque()
rt = deque()
res = []
for i in range(n):
    s = input().split()
    if "-" in s:
        res.append(lt.popleft())
    elif "+" in s:
        rt.append(s[-1])
    else:
        rt.appendleft(s[-1])
    if len(lt) < len(rt):
        lt.append(rt.popleft())
print(*res, sep="\n")
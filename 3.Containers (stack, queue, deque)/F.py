from collections import deque
n, k = map(int, input().split())
arr = list(map(int, input().split()))
q = deque()
for i in range(n):
    while q and arr[q[-1]] >= arr[i]:
        q.pop()
    q.append(i)
    if q[0] <= i - k:
        q.popleft()
    if i >= k - 1:
        print(arr[q[0]])
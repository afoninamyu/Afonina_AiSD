import heapq
n = int(input())
arr = []
for i in range(n):
    t, l = map(int, input().split())
    arr.append((t,l))
arr.sort()
h = []
for t, l in arr:
    end = t + l
    if h and t >= h[0]:
        heapq.heappop(h)
    heapq.heappush(h, end)
print(len(h))
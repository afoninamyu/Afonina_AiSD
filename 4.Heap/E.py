import heapq
n = int(input())
h = list(map(int, input().split()))
heapq.heapify(h)
res = 0
while len(h) >= 2:
    s = heapq.heappop(h) + heapq.heappop(h)
    res += s * 0.05
    heapq.heappush(h, s)
print(round(res, 2))
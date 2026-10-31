import heapq
n = int(input())
arr = []
h = []
for i in range(n):
    a = int(input())
    arr.append(a)
    heapq.heappush(h, (max(1000-a, 1), i))

time = 0
cur = 0

while True:
    t, i = heapq.heappop(h)
    if time + abs(cur - i) > t:
        break
    time = t
    cur = i
    arr[i] += 1
    heapq.heappush(h, (time + max(1000 - arr[i], 1), i))
print(t)
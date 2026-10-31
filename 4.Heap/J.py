import heapq
n, w = map(int, input().split())
arr = []
for i in range(n):
    ai, wi = map(int, input().split())
    arr.append((ai, ai + wi - 1, i + 1))
arr.sort(key=lambda x: x[0])

h = []
lvl = [[] for i in range (n + 1)]
num = 0
for left, right, i in arr:
    if h and h[0][0] < left:
        r, cur = heapq.heappop(h)
    else:
        num += 1
        cur = num
    lvl[cur].append(i)
    heapq.heappush(h, (right, cur))
print(num)
print(" ".join(str(i) for lay in lvl for i in lay))
class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def up(self, i):
        while i // 2 > 0 and self.heap[i] > self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def maxChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap[i * 2] > self.heap[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def down(self, i):
        while i * 2 <= self.size:
            j = self.maxChild(i)
            if self.heap[i] < self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def insert(self, k):
        self.heap.append(k)
        self.size += 1
        self.up(self.size)

    def extract(self):
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        self.size -= 1
        print(self.heap.pop())
        self.down(1)

heap = Heap()
n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:
        heap.insert(a[1])
    else:
        heap.extract()
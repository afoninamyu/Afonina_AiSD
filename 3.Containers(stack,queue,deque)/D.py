class Queue:
    def __init__(self):
        self.items = []

    def push(self, n):
        self.items.append(n)
        return "ok"

    def is_empty(self):
        return self.items == []

    def pop(self):
        if self.is_empty():
            return "error"
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return "error"
        return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return "ok"

q = Queue()
while True:
    func, *args = input().split()

    if func == "push":
        print(q.push(args[0]))

    elif func == "pop":
        print(q.pop())

    elif func == "front":
        print(q.front())

    elif func == "size":
        print(q.size())

    elif func == "clear":
        print(q.clear())

    elif func == "exit":
        print("bye")
        break
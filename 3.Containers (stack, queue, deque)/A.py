class Stack:
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
        return self.items.pop()

    def back(self):
        if self.is_empty():
            return "error"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return "ok"

s = Stack()
while True:
    func, *args = input().split()

    if func == "push":
        print(s.push(args[0]))

    elif func == "pop":
        print(s.pop())

    elif func == "back":
        print(s.back())

    elif func == "size":
        print(s.size())

    elif func == "clear":
        print(s.clear())

    elif func == "exit":
        print("bye")
        break

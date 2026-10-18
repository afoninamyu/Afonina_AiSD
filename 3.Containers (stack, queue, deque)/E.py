class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push_front(self, item):
        self.items = [item] + self.items
        return "ok"

    def push_back(self, item):
        self.items.append(item)
        return "ok"

    def pop_front(self):
        if self.is_empty():
            return "error"
        return self.items.pop(0)

    def pop_back(self):
        if self.is_empty():
            return "error"
        return self.items.pop()

    def front(self):
        if self.is_empty():
            return "error"
        return self.items[0]

    def back(self):
        if self.is_empty():
            return "error"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return "ok"

d = Deque()
while True:
    func, *args = input().split()

    if func == "push_front":
        print(d.push_front(args[0]))

    elif func == "push_back":
        print(d.push_back(args[0]))

    elif func == "pop_front":
        print(d.pop_front())

    elif func == "pop_back":
        print(d.pop_back())

    elif func == "front":
        print(d.front())

    elif func == "back":
        print(d.back())

    elif func == "size":
        print(d.size())

    elif func == "clear":
        print(d.clear())

    elif func == "exit":
        print("bye")
        break
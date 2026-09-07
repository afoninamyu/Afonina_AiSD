class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def dist(self):
        return (self.x**2 + self.y**2)**0.5

n = int(input())
pts = []
for i in range(n):
    x, y = map(int, input().split())
    pts.append(Point(x, y))

pts.sort(key=lambda i: i.dist())
for i in pts:
    print(i.x, i.y)
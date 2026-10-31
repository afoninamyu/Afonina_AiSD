from heapq import heappush, heappop

h = []
while True:
    try:
        s = input().split()
        if s[0] == "CLEAR":
            h = []
        elif s[0] == "ADD":
            heappush(h, -int(s[1]))
        elif s[0] == "EXTRACT":
            if h:
                print(-heappop(h))
            else:
                print("CANNOT")
    except EOFError:
        break
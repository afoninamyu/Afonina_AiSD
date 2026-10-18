from collections import deque
p1 = deque(map(int, input().split()))
p2 = deque(map(int, input().split()))
cnt = 0
while p1 and p2:
    cnt += 1
    a = p1.popleft()
    b = p2.popleft()
    if a > b and (a, b) != (9, 0) or (a, b) == (0, 9):
        p1.append(a)
        p1.append(b)
    else:
        p2.append(a)
        p2.append(b)
    if cnt == 10**6:
        print("botva")
        exit()
if p1:
    print("first", cnt)
else:
    print("second", cnt)
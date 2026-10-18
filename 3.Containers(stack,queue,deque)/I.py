n, *s = map(int, input().split())
row = []
cnt = 0
for b in s:
    if row and b == row[-1][0]:
        row[-1][1] += 1
        continue
    if row and row[-1][1] >= 3:
        cnt += row.pop()[1]
        if row and b == row[-1][0]:
            row[-1][1] += 1
            continue
    row.append([b, 1])
if row and row[-1][1] >= 3:
    cnt += row.pop()[1]
print(cnt)
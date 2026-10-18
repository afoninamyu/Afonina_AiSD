n = int(input())
ans = []
for j in range(n):
    k, *A = map(float, input().split())
    k = int(k)
    store = []
    B = sorted(A)
    i = 0
    for c in A:
        while store and i < k and store[-1] == B[i]:
            store.pop()
            i += 1
        if i < k and c == B[i]:
            i += 1
        else:
            store.append(c)
    while store and i < k and store[-1] == B[i]:
        store.pop()
        i += 1
    if i == k:
        ans.append(1)
    else:
        ans.append(0)
print(*ans, sep="\n")
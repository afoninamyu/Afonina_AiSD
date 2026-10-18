n = int(input())
r1 = list(map(int, input().split()))
de = []
nextt = 1
i = 0
while nextt <= n:
    if de and de[-1] == nextt:
        nextt += 1
        de.pop()
        continue
    if i < n:
        de.append(r1[i])
        i += 1
        continue
    print("NO")
    exit()
print("YES")
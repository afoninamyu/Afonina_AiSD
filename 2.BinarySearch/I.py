def bin_search_l(arr, x):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] <= x:
            l = m
        else:
            r = m
    if l == -1 or arr[l] != x:
        return -1
    return l

def bin_search_r(arr, x):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] < x:
            l = m
        else:
            r = m
    if r == len(arr) or arr[r] != x:
        return 0
    return r

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()
for i in range(M):
    print(bin_search_l(arr1, arr2[i]) - bin_search_r(arr1, arr2[i]) + 1, end=" ")
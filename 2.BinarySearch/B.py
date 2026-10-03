def bin_search(arr, x):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] < x:
            l = m
        else:
            r = m
    if l == -1:
        return arr[r]
    if r == len(arr):
        return arr[l]
    if abs(arr[l] - x) <= abs(arr[r] - x):
        return arr[l]
    else:
        return arr[r]
        

n, k = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
for i in range(k):
    print(bin_search(arr1, arr2[i]))
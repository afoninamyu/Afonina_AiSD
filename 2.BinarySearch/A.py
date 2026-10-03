def bin_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            return "YES"
        elif arr[m] < x:
            l = m + 1
        else:
            r = m - 1
    return "NO"

n, k = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
for i in range(k):
    print(bin_search(arr1, arr2[i]))

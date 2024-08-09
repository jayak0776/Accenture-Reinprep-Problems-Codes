def conDiff(n, arr):
    if n == 0:
        return 0
    consecDiff = []
    for i in range(1, n):
        consecDiff.append(arr[i] - arr[i - 1])
    return consecDiff

n = int(input())
arr = list(map(int, input().split()))
res = conDiff(n, arr)
print(*res)

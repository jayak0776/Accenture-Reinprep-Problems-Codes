def subarray(n, arr):
    count = 0
    for i in range(n - 2):
        if arr[i] + arr[i + 2] == arr[i + 1]:
            count += 1
    return count

n = int(input())
arr = list(map(int, input().split()))
print(subarray(n, arr))

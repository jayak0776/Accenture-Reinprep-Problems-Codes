def puzzle(n, arr):
    arr.sort()
    a = 1
    for i in arr:
        if i != a:
            return a
        a += 1
    return a

n = int(input())
arr = list(map(int, input().split()))
print(puzzle(n, arr))

def dinnerDish(n, arr):
    if n == 0 or n == 1:
        return 0
    arr.sort()
    return arr[-1] + arr[-2]

n = int(input())
arr = list(map(int, input().split()))
print(dinnerDish(n, arr))

def product(n, arr):
    prod = 1
    for i in arr:
        prod *= i
    return prod

n = int(input())
arr = list(map(int, input().split()))
print(product(n, arr))

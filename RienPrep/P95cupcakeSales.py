def cupcakeSales(n, arr):
    count = 0
    for i in arr:
        if i >= 5:
            count += i
    return count

n = int(input())
arr = list(map(int, input().split()))
print(cupcakeSales(n, arr))

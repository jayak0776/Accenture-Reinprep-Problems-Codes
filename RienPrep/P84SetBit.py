def setBit(n, arr, c):
    count = 0
    for i in arr:
        if bin(i).count('1') == c:
            count += 1
    return count

n = int(input())
arr = list(map(int, input().split()))
c = int(input())
print(setBit(n, arr, c))

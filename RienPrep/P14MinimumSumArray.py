def minimumSumArray(n,arr):
    arr.sort()
    a,b=arr[-1],arr[-2]
    avg=(a+b)/2
    for i in range(n):
        if arr[i] <avg:
            arr[i]=0
    return sum(arr)
n=int(input())
arr=list(map(int,input().split()))
print(minimumSumArray(n,arr))
        
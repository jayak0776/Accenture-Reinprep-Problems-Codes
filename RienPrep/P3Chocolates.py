def ChocolateProblem(n,arr):
    s=0
    for i in range(n):
        s+=arr[i]//3
        if arr[i]%3!=0:
            s+=1
    return s

arr=list(map(int,input().split()))
n=int(input())
print(ChocolateProblem(n,arr))

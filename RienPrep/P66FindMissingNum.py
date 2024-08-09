def missingNum(n,arr):
    maxi=max(arr)
    mini=min(arr)
    for i in range(mini,maxi+1):
        if i not in arr:
            return i
n=int(input()) 
arr=list(map(int,input().split())) 
print(missingNum(n,arr))
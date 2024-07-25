def peekElement(n,arr):
    for i in range(n):
        if i==0:
            if arr[i]>=arr[i+1]:
                return i
        elif i==n-1:
            if arr[i]>=arr[i-1]:
                return i    
        else:
            if arr[i-1]<=arr[i] and arr[i]>=arr[i+1]:
                return i
            
n=int(input())
arr=list(map(int,input().split()))
print(peekElement(n,arr))                
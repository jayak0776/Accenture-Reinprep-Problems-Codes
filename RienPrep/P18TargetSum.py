def targetSum(n,arr,target):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return [i,j]
 
n=int(input())
arr=list(map(int,input().split()))
target=int(input())
print(targetSum(n,arr,target))            
            
        
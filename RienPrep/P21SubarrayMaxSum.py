def subArrayMaxSum(n,arr):
    ans=arr[0]
    temp_max=arr[0]
    for i in arr[1:]:
        temp_max=max(temp_max+i,i)
        if temp_max>ans:
            ans=temp_max
    return ans        
    
n=int(input())
arr=list(map(int,input().split()))
print(subArrayMaxSum(n,arr))    
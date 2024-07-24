def equilibrium(n,arr):
    ans=0
    found=False
    for i in range(n):
        left,right=sum(arr[:i]),sum(arr[i+1:])
        if left==right:
            found=True
            ans=i+1
            break
    if found==False:
        return "NOT FOUND"
    else:
        return ans
n=int(input())
arr=list(map(int,input().split()))
print(equilibrium(n,arr))            

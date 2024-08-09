def maxSubArrSum(n,arr):
    maxSum=arr[0]
    curSum=0
    for i in arr:
        curSum=curSum+i
        maxSum=max(maxSum,curSum)
        if curSum<0:
            curSum=0
    return maxSum

n=int(input()) 
arr=list(map(int,input().split()))
print(maxSubArrSum(n,arr))
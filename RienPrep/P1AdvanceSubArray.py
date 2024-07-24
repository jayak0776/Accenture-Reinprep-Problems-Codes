def basketBallScore(n,k,arr):
    result=-1
    subArraySum=0
    for i in range(n-k+1):
        c=1
        for j in range(i,i+k):
            subArraySum+=c*arr[j]
            c+=1
        result=max(subArraySum,result)
        subArraySum=0
    return result        

n=int(input())
k=int(input())
array=list(map(int,input().split()))
print(basketBallScore(n,k,array))
def prefixSuffixBalance (N,A):
    totalSum=sum(A)
    firstPartSum=0
    result=[]
    for i in range(N):
        firstPartSum+=A[i]
        secondPartSum=totalSum-firstPartSum
        diff=abs(firstPartSum-secondPartSum)
        result.append(diff)
    return result

N=int(input())
A=list(map(int,input().split()))
print(prefixSuffixBalance(N,A))
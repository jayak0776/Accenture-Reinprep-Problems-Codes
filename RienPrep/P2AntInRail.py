def AntInRail(n,antMoves):
    originalPositionCount=0
    sum=0
    for i in antMoves:
        sum+=i
        if sum==0:
            originalPositionCount+=1
    return originalPositionCount        
n=int(input())
antMoves=list(map(int,input().split()))
print(AntInRail(n,antMoves))
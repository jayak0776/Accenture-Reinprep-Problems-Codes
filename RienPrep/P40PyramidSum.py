def pyramidSum(n):
    totalSum=0
    for i in range(1,n+1):
        for j in range(i,0,-1):
            totalSum+=j
        for j in range(2,i+1): 
            totalSum+=j
    return totalSum

n=int(input())
print(pyramidSum(n))
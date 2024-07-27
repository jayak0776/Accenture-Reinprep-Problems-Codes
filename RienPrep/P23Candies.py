def last(n,k,a):
    lastPos=(a+k-1)%n
    if lastPos==0:
        return n
    else:
        return lastPos
    
data=list(map(int,input().split())) 
n,k,a= data[0],data[1],data[2]
print(last(n,k,a))  
    
def MathTest(n):
    f=True
    next=n+1
    while f:
        li=[]
        for i in range(2,next//2+1):
            if next%i==0:
                li.append(i)
                break
        if len(li)==0:
            f=False
        else:
            next+=1
    return next    

n=int(input())
print(MathTest(n))            
            
            
                
                
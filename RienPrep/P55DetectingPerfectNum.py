def perfectNum(n):
    divisor=[]
    for i in range(1,n//2+1):
        if n%i==0:
            divisor.append(i)
    if sum(divisor)==n:
        return "1"
    else: 
        return sum(divisor)

n=int(input())
print(perfectNum(n))
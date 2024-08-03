def solveThisEquation(n):
    count=0
    for a in range(1,n+1):
        for b in range(1,n+1): 
            for c in range(1,n+1):
                if (a**2+b**2+c**2+a*b+b*c+c*a)==n: 
                    count+=1
    return count

n=int(input())
print(solveThisEquation(n))
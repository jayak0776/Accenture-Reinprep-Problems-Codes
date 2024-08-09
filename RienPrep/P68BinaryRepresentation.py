def binary(n): 
    s="" 
    t=0 
    while n>0: 
        if n%2==0: 
            s+="0" 
        else: 
            s+="1" 
            n=n//2 
    for i in s: 
        t+=int(i) 
    return t 

n=int(input())
print(binary(n))
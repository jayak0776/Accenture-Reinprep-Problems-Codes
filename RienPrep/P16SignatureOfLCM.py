import math
def lcmGcd(a,b):
    g=math.gcd(a,b)
    l=(a*b)//g
    print(g)
    print(l)
 
a,b=map(int,input().split())
lcmGcd(a,b)    
    
    
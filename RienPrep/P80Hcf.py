import math
def hcf(x,y):
    return math.gcd(x,y)

x,y=map(int,input().split())
ans=hcf(x,y)
# print(f"The HCF of {x} and {y} is: {ans}")
print(ans)
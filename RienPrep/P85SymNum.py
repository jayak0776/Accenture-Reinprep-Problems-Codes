def symNum(n):
    a = bin(n)[2:]  
    length = len(a)
    return "1" * length  

n = int(input())
res = symNum(n)
print(int(res, 2)) 

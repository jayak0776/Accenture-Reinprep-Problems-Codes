def EncodedString(n):
    res=''
    while n>0:
        c=n%10
        res=str(c**2)+res
        n=n//10
    return res

n=int(input())
print(EncodedString(n))
    
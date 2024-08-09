def rotateString(n,s,k):
    res=""
    if k==0:
        return s
    else:
        if k>n:
            while k>n:
                k=k-n
        res=s[k:]+s[0:k]
    return res

n=int(input())
s=input()
k=int(input())
if n==0:
    print("NULL")
else:
    print(rotateString(n,s,k))
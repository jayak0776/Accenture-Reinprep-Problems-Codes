def palindCon(n):
    
    def reverseNum(m):
        m=list(str(m))
        m.reverse()
        return int(''.join(m))

    if len(str(n))==1:
        return n
    result=0
    flag=True
    while flag:
        rev=reverseNum(n)
        s=n+rev
        if s==reverseNum(s):
            result=s
            flag=False
        n=s
    return result

n=int(input())
print(palindCon(n))
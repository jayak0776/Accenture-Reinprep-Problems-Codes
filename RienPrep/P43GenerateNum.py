def genNum(n,a,b):
    s=set()
    def um(m):
        if m<=0:
            return m
        if m not in s:
            s.add(m)
            um(m-a)
            um(m-b)
    um(n)
    return len(s)

n,a,b=map(int,input().split())
print(genNum(n,a,b))      
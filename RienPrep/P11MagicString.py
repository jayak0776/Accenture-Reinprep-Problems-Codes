def MagicString(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return len(s)-max(d.values())

s=input()
print(MagicString(s))            
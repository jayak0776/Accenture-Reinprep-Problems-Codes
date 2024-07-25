def missingAlphabets(s):
    alphabets=set("abcdefghijklmnopqrstuvwxzy")
    diff=sorted(alphabets.difference(s))
    return diff

s=input()
res=missingAlphabets(s)
print("".join(res))
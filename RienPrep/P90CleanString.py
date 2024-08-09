def cleanString(s1, s2):
    res = ""
    for i in s1:
        if i not in s2:
            res += i
    if res:
        return res
    else:
        return "Empty"
s1 = input()
s2 = input()
print(cleanString(s1, s2))

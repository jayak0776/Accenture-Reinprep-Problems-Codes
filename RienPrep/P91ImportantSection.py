def importantSection(s):
    c = 0
    idx = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "1":
            idx = i
            c = 1
            break
    if c:
        return idx
    else:
        return -1
s = input()
print(importantSection(s))

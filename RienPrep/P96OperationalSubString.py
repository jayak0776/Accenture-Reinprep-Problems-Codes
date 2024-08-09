from collections import Counter
def operationalString(s):
    d = Counter(s)  
    res = 0
    for key, value in d.items():
        res += (value * (value + 1)) // 2 
    return res
s = input()
print(operationalString(s))

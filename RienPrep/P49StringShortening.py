def stringShorten(s):

    flag=True

    while flag: 
        newStr=""
        i=0
        while i<len(s):
            if i<len(s)-1 and s[i]==s[i+1]:
                i+=2
            else: 
                newStr+=s[i] 
                i+=1 
        if newStr==s: 
            flag=False 
        s=newStr 
    return "Empty String" if s=="" else s

s=input()

print(stringShorten(s))
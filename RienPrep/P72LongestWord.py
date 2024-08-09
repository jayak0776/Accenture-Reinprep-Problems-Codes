def findLongString(s): 
    s=s.split(' ') 
    l=0 
    res="" 
    for i in s: 
        if len(i)>l: 
            l=len(i) 
            res=i 
    return res

s=input() 
result=findLongString(s) 
print("The longest string is:", result)
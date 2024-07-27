def bestGrade(s,p,k):
    p-=1
    maxi=max(0,p-k)
    
    minc=min(s[maxi:p+1])
    mini=s.index(minc,maxi,p+1)
    
    s=list(s)
    for i in range(mini,p):
        s[i],s[i+1]=s[i+1],s[i]
    
    s=''.join(s)
    return s[p]  

s=input()
p=int(input())
k=int(input())
print(bestGrade(s,p,k))  
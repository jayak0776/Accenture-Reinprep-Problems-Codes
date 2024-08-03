def pizzParty(x,y):
    s=0
    while x%y!=0:
        y+=1
    y=str(y)
    for i in y:
        s+=int(i) 
    return s       

x,y=map(int,input().split())
print(pizzParty(x,y))
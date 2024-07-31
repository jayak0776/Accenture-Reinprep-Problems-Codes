def objectScore(cap,pro):
    result=[]
    for c in cap:
        total=0
        for p,w in pro:
            if p<=c:
                total+=w
        result.append(total)
    return result            
            

n,m=map(int,input().split())
cap=list(map(int,input().split()))
products=[]
for i in range(m):
    p,w=map(int,input().split())
    products.append([p,w])
result=objectScore(cap,products)    
print(*result,sep=" ") 
   
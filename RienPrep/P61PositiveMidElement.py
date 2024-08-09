def posMid(n,arr):
    midEle=0
    posEle=[]
    for i in arr:
        if i>0:
            posEle.append(i)
    if len(posEle)%2==0:
        mid=len(posEle)//2 
        if posEle[mid]>posEle[mid-1]: 
            midEle=posEle[mid-1]
        else: 
            midEle=posEle[mid]
    else: 
        mid=len(posEle)//2 
        midEle=posEle[mid]

    return midEle

n=int(input()) 
arr=list(map(int,input().split())) 
print(posMid(n,arr))
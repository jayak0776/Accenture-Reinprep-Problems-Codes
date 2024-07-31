def reversePack(n,arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    result=[]
    for key,value in d.items():
        for _ in range(key):
            result.append(value)
    result.sort()
    return result
n=int(input())
arr=list(map(int,input().split()))
print(reversePack(n,arr))
                    
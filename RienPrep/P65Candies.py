def candie(n,arr,u):
    count=0
    arr.sort()
    for i in arr:
        if u>=i:
            u-=i
            count+=1
        else:
            break
    return count

n=int(input())
arr=list(map(int,input().split()))
u=int(input())
print(candie(n,arr,u))
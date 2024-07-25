def arduino(arr):
    maxDis=0
    curr=0
    for i in arr:
        curr+=i
        if abs(curr)>maxDis:
            maxDis=abs(curr)
    return maxDis

arr=list(map(int,input().split()))
print(arduino(arr))
        
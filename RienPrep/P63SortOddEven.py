def sortOddEven (n,arr):
    result=[]
    for i in range(n):
        if arr[i]%2==0:
            result.append(arr[i])
    for i in range(n): 
        if arr[i]%2!=0: 
            result.append(arr[i])
    return result

n=int(input()) 
arr=list(map(int,input().split())) 
print(sortOddEven(n,arr))
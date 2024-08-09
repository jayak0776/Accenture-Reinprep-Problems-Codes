def specialArray(n,arr):
    flag="YES"
    for i in range(0,n-1): 
        if arr[i]%2==0: 
            if arr[i+1]%2==0: 
                flag="NO" 
                break
        else: 
            if arr[i+1]%2!=0: 
                flag="NO" 
                break

    return flag


n=int(input())
arr=[] 
for _ in range(n): 
    ele=int(input()) 
    arr.append(ele) 
print(specialArray(n,arr))
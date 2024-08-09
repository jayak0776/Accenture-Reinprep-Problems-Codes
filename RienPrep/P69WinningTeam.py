from collections import Counter
n=int(input())
arr=[]
for i in range(n): arr.append(input())
d=Counter(arr)
maxi=float("-inf")
ans=0
for key, value in d.items(): 
    if value>maxi: 
        maxi=value 
        ans=key
print(ans)
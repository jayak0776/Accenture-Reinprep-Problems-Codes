def countSubString(n,str,k):
    count=0
    for i in range(n):
        ones, zeros=0,0
        for j in range(i,n):
            if str[j]=='1':
                ones+=1
            else:
                zeros+=1
            if ones <=k and zeros <=k : 
                count+=1
            else:
                break
    return count

n=int(input())
str=input()
k=int(input())
print(countSubString(n,str,k))
def count(n):

    count=0

    for x in range(1,n+1):
        if len(str(x))%2!=0:
            count+=1

    return count

n=int(input())
print(count(n))
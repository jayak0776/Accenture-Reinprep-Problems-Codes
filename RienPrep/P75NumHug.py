def is_prime(n):
    if n==2:
        return True
    if n%2==0 or n<2:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

def calHuge(n):
    li=[]
    li.append(1)
    for i in range(2,n+1):
        li.append(i|li[i-2]) 
    li.sort(reverse=True)
    for i in li:
        if is_prime(i):
            return i
    return -1

n=int(input())
print(calHuge(n))
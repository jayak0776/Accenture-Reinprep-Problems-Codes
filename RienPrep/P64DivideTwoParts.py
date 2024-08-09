def divideTwoParts(n):
    if n%2==0 and (n//2)%2==0 :
        return "YES"
    return "NO"
n=int(input())
print(divideTwoParts(n))
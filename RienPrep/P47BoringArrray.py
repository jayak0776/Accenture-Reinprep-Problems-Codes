def maxscore(n,a):
    a.sort()
    score=0
    i,j=0,n-1
    while i<j:
        score+=a[j]-a[i]
        i+=1
        j-=1
    return score

n=int(input())
arr=list(map(int,input().split()))

print(maxscore(n,arr))
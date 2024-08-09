def gamesTimer(n,arr):
    gamesCount=0 
    for i in arr: 
        mins=i*60
        gamesCount+=mins//10
    return gamesCount

n=int(input())
arr=list(map(int,input().split())) 
print(gamesTimer(n,arr))
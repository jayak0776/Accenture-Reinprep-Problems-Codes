def roboRace(x,n,y,m):
    if x<y:
        x,y=y,x
        n,m=m,n
    ans=y-x
    pos=0
    for pos in range(n):
        if(ans%n + pos*m)%n ==0:
            break
    if pos!=n:
        return y+pos*m        

x,n,y,m=map(int,input().split())
print(roboRace(x,n,y,m))

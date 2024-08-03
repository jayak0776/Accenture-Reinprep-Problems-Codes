def pattern(n):
    temp=n
    for k in range(n,0,-1):
        for i in range(n,0,-1):
            for j in range(temp):
                print(i,end=" ")
        print()
        temp-=1

n=int(input())

pattern(n)
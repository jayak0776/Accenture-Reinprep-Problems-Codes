def oddEvenCarFine(d,n,cars):
    total_fine=0
    fine=250
    if d%2==0:
        for i in cars:
            if i%2!=0:
                total_fine+=fine
    else:
        for i in cars: 
            if i%2==0: 
                total_fine+=fine
    return total_fine

d=int(input())
n=int(input())
if n==0:
    print(-1)
else: 
    cars=list(map(int,input().split())) 
    print(oddEvenCarFine (d,n,cars))
from collections import Counter
def numberMatch(n,arr):
    counts=Counter(arr)
    a,b=0,0
    for num,c in counts.items():
        if num%2==0:
            if c%2==0:
                a+=1
            else:
                b+=1
        else:
            if c%2==0:
                b+=1
            else:
                a+=1
    if a>b:
        print("A",a-b)
    elif a<b:
        print("B",b-a)
    else:
        print("T",0)                                    
            

n=int(input())
arr=list(map(int,input().split()))
numberMatch(n,arr)

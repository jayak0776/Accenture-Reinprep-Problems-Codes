def reduceZero(x,y):
    while y!=0:
        if x<y:
            x,y=y,x
        else:
            t=x-y
            x=y
            y=t
    return x            

x=int(input())
y=int(input())
print(reduceZero(x,y))
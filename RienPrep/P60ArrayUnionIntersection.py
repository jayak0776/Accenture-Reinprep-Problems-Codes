def ul(a,b):
    intersection=[]
    for i in a:
        if i in b:
            intersection.append(i)
    intersection.sort()
    print(intersection)
    a.extend(b)
    a=sorted(list(set(a)))
    print(a)

a=list(map(int, input().split()))
b=list(map(int, input().split()))
ul(a,b)
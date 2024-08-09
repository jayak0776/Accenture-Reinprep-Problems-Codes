def smallestNum(n):
    while len(str(n))<5: 
        n+=1 
        for i in str(n): 
            if str(n).count(i)>1:
                break
        else:
            return n

n=int(input()) 
print(smallestNum(n))
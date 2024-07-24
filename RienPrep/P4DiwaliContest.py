def DiwaliContest(p,arrialTime):
    time=4*60 -arrialTime
    solve=0
    for i in range(1,p+1):
        if time>0 and time-i*5 >0:
            time-=i*5
            solve+=1
    return solve        

p=int(input())
arrialTime=int(input())
print(DiwaliContest(p,arrialTime))
def tossAndScore(s):
    score=0
    count=0
    for i in s:
        if i=="H":
            score+=2
            count+=1
            if count==3:
                break
        else:
            score-=1
            count=0
    return score
s=input()
print(tossAndScore(s))            
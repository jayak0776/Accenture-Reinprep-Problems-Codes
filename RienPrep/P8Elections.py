def ElectionWinner(n,arr):
    votesCount={}
    for i in arr:
        if i in votesCount:
            votesCount[i]+=1
        else:
            votesCount[i]=1
    
    maxVotes=max(votesCount.values())
    winner=-1
    for party,votes in votesCount.items():
        if votes==maxVotes:
            if winner==-1:
                winner=party
            else:
                winner=-1
    return winner

n=int(input())
arr=list(map(int,input().split()))
print(ElectionWinner(n,arr))
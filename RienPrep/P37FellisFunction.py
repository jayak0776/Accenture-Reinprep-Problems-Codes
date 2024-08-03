def fellis_function(N):
    MOD = 10**9 + 7

    if N == 0:
        return 1
    if N == 1:
        return 1
    
    prev2,prev1=1,1
    for i in range(2, N + 1):
        current = (prev1 + 7 * prev2 + (i // 4)) % MOD
        prev2 = prev1
        prev1 = current

    return prev1

n=int(input())
print(fellis_function(n)) 
def sf(n):
    f=[1,1]
    for N in range(2,n+1):
        val=(f[N-1]*f[N-1]+f[N-2]*f[N-2])%47
        f.append(val)
    return f[-1]

n=int(input())
print(sf(n))    
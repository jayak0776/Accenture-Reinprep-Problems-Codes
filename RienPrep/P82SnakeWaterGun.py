def ways(n, s, m):
    a = []
    while s:
        for i in m:
            if s.startswith(i):
                a.append(i)
                s = s[len(i):]
                break
    return a

def snakeWaterGun(n, s):
    count, m = 0, ["snake", "water", "gun"]
    arr = ways(n, s, m)
    
    for i in range(0, len(arr) - 1, 2):
        if i + 1 < len(arr):
            if arr[i] == "snake" and arr[i + 1] == "water":
                count += 1
            elif arr[i] == "water" and arr[i + 1] == "gun":
                count += 1
            elif arr[i] == "gun" and arr[i + 1] == "snake":
                count += 1
                
    return count

n = int(input())
s = input()
print(snakeWaterGun(n, s))

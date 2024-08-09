def vacantRooms(n, t):
    return t - n
n = int(input())
a = list(input().split())
t = int(input())
print(vacantRooms(n, t))

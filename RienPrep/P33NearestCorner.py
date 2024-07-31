def nearestCorner(seat,arr):
    element=None
    for row in arr:
        if seat in row:
            element=row
            break
    element=element.split()
    left_corner=element.index(seat)
    right_corner=(len(element)-1)-element.index(seat)
    if right_corner==0:
        right_corner=999999
    return min(left_corner,right_corner)        

seat=input()
arr=input().split(" - ")
print(nearestCorner(seat,arr))
    
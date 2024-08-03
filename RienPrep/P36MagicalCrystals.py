def magicalCrystals(x,y,z):
    highSum=x+y
    if highSum<(y+z):
        highSum=y+z
    if highSum<(x+z):
        highSum=x+z 
    return highSum


x,y,z=map(int,input().split())
print(magicalCrystals(x,y,z))

       
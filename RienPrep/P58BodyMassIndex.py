def bodyMassIndex(w,h):
    bmi=w//(h**2)
    if bmi<18:
        return 0
    elif 18 <=bmi<25:
        return 1
    elif 25<=bmi<30:
        return 2
    elif 30<=bmi<40:
        return 3
    else:
        return 4

w=int(input())
h=float(input())
print(bodyMassIndex(w,h))
def minimumBadness(s):
    li = []
    c = 0
    for i in s:
        if li:
            if li[-1] != i and i != "W":
                li.append(i)
                c += 1
        else:
            if i != "W":
                li.append(i)

    return c

s = input()
print(minimumBadness(s))

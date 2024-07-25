def reverseOrderOfString(s):
    s=s.split(" ")
    s=s[::-1]
    return " ".join(s)

s=input()
print(reverseOrderOfString(s))

   
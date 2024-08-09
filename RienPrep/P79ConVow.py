def numVowCon(s):
    vowels=0
    consonants=0
    for i in s:
        if i in "aeiou":
            vowels+=1
        else:
            consonants+=1 
    print("Number of vowels:", vowels)
    print("Number of consonants:", consonants)

s=input() 
numVowCon(s)
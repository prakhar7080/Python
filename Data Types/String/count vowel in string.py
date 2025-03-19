def count(s):
    vowel = "aeiouAEIOU"
    num = 0
    for c in s:
        if c in vowel:
            num+=1
    return num
print(count("I love india"))
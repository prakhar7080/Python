def count(s):
    vowel = "aeiouAEIOU"
    n = 0
    for c in s:
        if c in vowel:
            n+=1
    return n
print("No of vowel = ",count("Hello i am on this side"))
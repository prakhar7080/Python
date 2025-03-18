def calc(s):
    digit = 0
    upper = 0
    lower = 0
    for c in s:
        if c.isdigit():
            digit+=1
        elif c.isupper():
            upper+=1
        elif c.islower():
            lower+=1
    return [digit,upper,lower]

lst = calc("HeLLO 123 abc")
print("Digit = ",lst[0]," Upper = ",lst[1]," lower = ",lst[2])

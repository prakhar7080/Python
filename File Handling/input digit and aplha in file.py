# Describe a python program to write number of letters and digits in a given input string into a given file object
def count_(str):
    letter = 0
    digit = 0
    for i in str:
        if i.isdigit():
            digit+=1
        elif i.isalpha():
            letter+=1
    return letter,digit
def save(name,l,d):
    with open(name,"w") as f:
        f.write(f"No of words = {l}\n")
        f.write(f"No of digits = {d}")
str = input("Enter letters and digits = ")
l,d = count_(str)
filename = "count.txt"
save(filename,l,d)
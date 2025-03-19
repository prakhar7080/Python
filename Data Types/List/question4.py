# Construct a program that accept a comma separated sequence of word as input and print the word in comma separated sequence after sorting them

data = input("Enter comma separated words ")
lst = data.split(",")
lst = sorted(lst)
print(",".join(lst))
# for l in lst:
#     print(l,end=",")
# Write a python program to add item in tuple

tup = (1,2,3,4)
print(tup)
#Now we have to add 5 in this tuple
#1. Method
tup = tup+(5,)
print(tup)
#2. Method
#Now add 6
lst = list(tup)
lst.append(6)
tup = tuple(lst)
print(tup)
import random
lst = []
n = int(input("Enter the value of n = "))
for i in range(0,n):
    k = int(input())
    # lst.extend([k])
    lst.append(k)
print(lst)
print("Originol list --> "+ str(lst))
random.shuffle(lst)
print("Random List --> "+ str(lst))


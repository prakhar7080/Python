n = int(input("Enter the value of n = "))
n1 = 0
n2 = 1
if n<0:
    print("Enter positive number")
elif n==1:
    print(n1)
else:
    print(n1)
    print(n2)
    for i in range(3,n+1):
        nth = n1+n2
        print(nth)
        n1 = n2
        n2 = nth

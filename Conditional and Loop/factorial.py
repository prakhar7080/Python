number = int(input("Enter the value of n = "))
fact = 1
while number:
    fact=fact*number
    number-=1
print("Factorial = ",fact)
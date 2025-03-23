number = int(input("Enter the value of n = "))
fact = 1
temp_number = number
while number:
    fact=fact*number
    number-=1
print("Factorial of ",temp_number," = ",fact) 
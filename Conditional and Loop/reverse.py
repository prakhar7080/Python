num = int(input("Enter the number = "))
rev = 0
while num>0:
    d = num%10
    rev = rev*10+d
    num = num//10
print("Reversed number = ",rev)
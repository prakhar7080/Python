n = int(input("Enter a number = "))
count=0
num = n
while n>0:
    count+=1
    n=n//10
number = num
digit = 0
while num>0:
    r = num%10
    digit+=r**count
    num = num//109
if number == digit :
    print("Armstrong")
else:
    print("Not armstrong")

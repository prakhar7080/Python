num = int(input("Enter the number = "))
flag = 1
if num<0:
    print("Enter positive number")
elif num==1:
    print("1 is not a prime number")
else:
    for i in range(2,num):
        if num%i == 0:
            flag = 0
            break
if flag == 0:
    print("Not prime")
else:
    print("Prime")
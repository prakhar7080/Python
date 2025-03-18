def isperfect_square(x):
    num = int(x**0.5)
    return num*num == x
def isfibonacci(n):
    return isperfect_square(5*n*n+4) or isperfect_square(5*n*n-4)

i = int(input("Enter number = "))
if(isfibonacci(i) == True):
    print(i,"is fibonacci")
else:
    print(i,"is not fibonacci")
string = input("Enter a string = ")
s = string
rev = s[::-1]
if rev == string:
    print(string,"is palindrome")
else:
    print(string,"is not palindrome")
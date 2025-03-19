# Write a python program to enter a space seperated input with numbers and extract numbers

def create_file(file):
    data = input("Enter space seperated sequence = ")
    with open(file,"w") as file1:
        file1.write(data)
def find_digit(file):
    with open(file,"r") as file1:
        data = file1.read()
    words = data.split(5)
    digi = [word for word in words if word.isdigit()]
    return digi
create_file("space.txt")
lst = find_digit("space.txt")
for l in lst:
    print(l)



# Write a python program to print last n lines of file
def func(file1,n):
    lst = []
    with open(file1,"r") as file:
        for line in file:
            lst.append(line.strip())
    return lst[-n:]
data = func("myfile.txt",2)
for l in data:
    print(l)
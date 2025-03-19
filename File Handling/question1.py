# Write a python program to read a file line by line store it into a list
def func(a):
    lst=[]
    with open(a,"r") as file1:
        while True:
            str = file1.readline()
            if not str:
                break
            else:
                lst.append(str.strip())
    return lst
a = func("myfile.txt")
print(a)
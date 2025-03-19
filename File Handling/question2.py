# Write a python program to read a file line by line and store it into a variable

def func(file1,n):
    with open(file1,"r") as file:
        for i in range(n):
            str = file.readline()
            if not str:
                break
            else:
                print(str,end=" ")
func("myfile.txt",2)
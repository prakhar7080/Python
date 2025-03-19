file1 = open("myfile.txt","w")
str = "Write line\n"
file1.write(str)

lst = ["write lines 1\n","write lines 2\n","write lines 3\n"]
file1.writelines(lst)
file1.close()

# file1 = open("myfile.txt","r")
# print(file1.read())
with open("myfile.txt","r") as file1:
    lst = file1.readlines()
print("List of strings = ",lst)
print("Each line of list = ")
for line in lst:
    print(line)
with open("myfile.txt","r") as file1:
    str = file1.readline()
print("Single line = ",str)

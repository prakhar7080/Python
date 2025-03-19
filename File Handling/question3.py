# Write a python program to apend a line to file and print it
def func(file1,text):
    with open(file1,'a') as file:
        file.write(text+"\n")
    with open(file1,'r') as file:
        data = file.read()
    return data
print(func("myfile.txt","This is apended text"))
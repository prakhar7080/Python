with open("comma.txt","r") as file:
    str = file.read()
    sep = ",".join(str)
with open("comma.txt","w") as file:
    file.write(sep)

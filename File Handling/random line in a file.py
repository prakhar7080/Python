import random
def random_line(file_name):
    with open(file_name,"r") as file:
        lst = file.readlines()
    line = random.choice(lst)
    return line
print(random_line("myfile.txt"))
    
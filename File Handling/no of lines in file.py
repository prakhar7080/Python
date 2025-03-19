def no_of_lines(file_name):
    with open(file_name,"r") as file:
        lst = file.readlines()
    return len(lst)
print(no_of_lines("comma.txt"))
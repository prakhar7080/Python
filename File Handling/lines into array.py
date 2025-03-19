def lines_to_array(file_name):
    lst = []
    with open(file_name,"r") as file:
        for line in file:
            lst.append(line.strip())
    return lst

file_name = "myfile.txt"
lines_list = lines_to_array(file_name)
for line in lines_list:
    print(line)
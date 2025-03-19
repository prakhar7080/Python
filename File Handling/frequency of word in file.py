from collections import Counter
def count(file_name):
    with open(file_name,"r") as file:
        return Counter(file.read().split())
print(count("myfile.txt"))
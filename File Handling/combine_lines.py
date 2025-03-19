with open("space.txt","r") as file1, open("myfile.txt","r") as file2:
    for line1,line2 in zip(file1,file2):
        print(line1.strip()+" "+line2.strip())
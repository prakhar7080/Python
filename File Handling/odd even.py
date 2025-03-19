def enter_number(file_name):
    with open(file_name,"w") as file:
        file.writelines("18\n")
        file.writelines("45\n")
        file.writelines("67\n")
        file.writelines("40\n")
        file.writelines("89\n")
        file.writelines("80\n")
def odd_even(file_name):
    with open(file_name,"r") as file:
        lst = file.read()
        num = lst.split()
    with open("odd.txt","w") as odd:
        with open("even.txt","w") as even:
            for l in num:
                if int(l)%2 == 0:
                    even.write(l+" ")
                else:
                    odd.write(l+" ")

enter_number("number.txt")
odd_even("number.txt")

    

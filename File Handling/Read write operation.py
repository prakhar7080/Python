# Write 
file1 = open("example.txt","w")
file1.write("Hello there")
file1.close()

#Read
file1 = open("example.txt","r")
data = file1.read()
print(data)

#Apend
file1 = open("example.txt","a")
file1.write(" I am here")
file1.close()
'''
* * * * *
* * * *
* * *
* *
*
'''

row = int(input("Enter no of rows = "))
for i in range(row,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")
'''
      *
     * *
    * * *
   * * * *
  * * * * * 
'''

row = int(input("Enter number of rows = "))
for i in range(0,row):
    for j in range(row-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end = "")
    print()

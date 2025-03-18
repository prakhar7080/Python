list1 = [1,2,3,4,5,6,7,8,9]

#1.Return the list of numbers starting from the last to second item in the list

print(list1[-1:-3:-1])

#2.Return a list that start form 3rd item to second last item

print(list1[2:-1])

#3.Return a list that have only even position element of list 

print(list1[0::2])

#4.Return a list that start form middile of list

middile = len(list1)//2
print(list1[middile:])

#5.Return a list that reveses all the element starting from element at index 0 to middile index only and return the entire list

ans = list1[0:middile+1][::-1]+list1[middile+1:]
print(ans)

#6.Divide each element of the list by 2 and replace it with the remainder

list2 = [x%2 for x in list1]
print(list2)
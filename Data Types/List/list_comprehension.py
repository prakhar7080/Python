#It is used to create a new list from an existing list

# eg
# number = [1,2,3,4,5]
# double = [x*2 for x in number]
# print(double)

#even number less than 10 + 3

# ans = [x+3 for x in range(11) if x%2 == 0]
# print(ans)

# Question --> Write a function less than (lst,k) to return a list of number less than k from the list
# The function use the list comprehension

def solve(lst,k):
    ans = [x for x in lst if x<k]
    print(ans)
lst = [1,-2,0,5,-3]
k = 0
solve(lst,k)
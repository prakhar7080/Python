# Write a function make pair that takes as input two lists of equal length and return a single list of same length where kth element is the pair of k element from the input list

def makepair(list1,list2):
    l=[(list1[i],list2[i]) for i in range(0,len(list1))]
    return l
list1 = [1,3,5,7]
list2 = [2,4,6,8]
ans = makepair(list1,list2)
print(ans)
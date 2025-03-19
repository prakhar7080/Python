# Write a python function, searchMany(s,x,k) that takes an argument a sequence s and integer x,k (k>0) the function returns true is there are k occurrence of x in s. Otherwise it return false searchMany ([10,17,15,12],15,1) return true, searchMany([10,12,12,12],12,2) return false

#1. Method
# def searchMany(s,x,k):
#     coun = s.count(x)
#     if coun == k:
#         return True
#     return False
# print(searchMany([10,12,12,12],12,2))

#2. Method
def searchMany(s,x,k):
    n = 0
    for i in s:
        if i==x:
            n+=1
    if n == k:
        return True
    return False
print(searchMany([10,17,15,12],15,1))
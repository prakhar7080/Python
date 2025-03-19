# Write a python function removekth (s,k) that takes as input a string and integer k>=0 and remove the character at index k. if k is beyond the length of s, the whole of s is returned.

#Using convert in list
# def removekth(s,k):
#     lst=[]
#     for i in s:
#         lst.append(i)
#     if len(lst)<=k:
#         return s
#     lst.pop(k)
#     str = ""
#     for i in lst:
#         str = str + i
#     return str
# print(removekth("python",4))

#using string slicing

def removekth(s,k):
    if(k<0):
        return s
    elif len(s)<=k:
        return s
    else:
        return s[:k]+s[k+1:]
    
print(removekth("python",4))
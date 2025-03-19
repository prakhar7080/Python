# Construct a function ret_smaller(l) that return smaller list from a nested list
# if two list have same length then return the first list that is encountered
# lst = [[3,4,5],[6,7],[10],[5,6]]
def ret_smaller(l):
    if not l:
        return []
    else:
        x = l[0]
        for a in l[1:]:
            if len(x)>len(a):
                x = a
    return x
print(ret_smaller([[2,3,4],[5],[6,7],[8,9]]))
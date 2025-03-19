from itertools import permutations
def perm(s):
    lst = list(permutations(s))
    # lst1 = ["".join(word) for word in lst]
    lst1 = []
    for word in lst:
        lst1.append("".join(word))
    return lst1
print(perm("abc"))
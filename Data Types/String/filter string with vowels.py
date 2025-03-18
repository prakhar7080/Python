vowel = ["a","e","i","o","u","A","E","I","O","U"]
def filter_(lst):
    return [x for x in lst if x[0] in vowel]
lst = ["monkey","abc","elephant","rat","ubuntu"]
print(filter_(lst))
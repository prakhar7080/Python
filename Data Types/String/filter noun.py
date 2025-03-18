noun = ["agra","banana","ramesh","patna"]
def filter_(lst):
    return [x for x in lst if x in noun]
lst = ["bus","banana","car","mohan","agra","delhi"]
print(filter_(lst))
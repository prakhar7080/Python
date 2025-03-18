
def filter_number(lst):
    return [x for x in lst if x.isdigit()]
lst = ["prakhar","123","gupta","56","9","gate"]
print(filter_number(lst))
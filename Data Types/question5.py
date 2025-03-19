# Write a python program, count_square(N) that returns the count of perfect square less than or equal to N(N>=1) for example count_square(1) return 1 only perfect square less than equal to 1 coun_square(5) return 2(1,4 are the perfect quare less than equal to 2)
#count_square(55) return 7 (1,4,9,16,25,36,49)<=55
def count_square(N):
    lst=[]
    for i in range(1,N+1):
        sqrt = int(i**0.5)
        if sqrt**2 == i:
            lst.append(i)
    return len(lst)
print(count_square(6))
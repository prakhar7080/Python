# Write a program factor(N) that return a list of all positive divisor of N (N>=1).
def factor(N):
    lst = []
    if N>=1:
        for i in range(1,N+1):
            if N%i == 0:
                lst.append(i)
        return lst
print(factor(6))
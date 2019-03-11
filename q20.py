from math import factorial

def sod(n):
    summ = 0
    while n!= 0:
        summ +=n%10
        n = n//10
    return summ
print(sod(factorial(100)))
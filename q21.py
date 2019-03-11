arr = list()
summ = 0
def sumofdiv(a):
    global summ
    summ = 0
    for i in range(1,a-1):
        if a%i == 0:
            summ+=i
    return summ
summation = 0
for _ in range(1,10001):
    a = sumofdiv(_)
    b = sumofdiv(a)
    if b == _ and a!=b:
        print(b)
        summation+=b
print(summation)
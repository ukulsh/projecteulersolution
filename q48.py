import sys
a = sys.float_info.epsilon
summ = 0
for i in range(1,1001):
    summ+=pow(i,i,10**10)
print(str(summ)[-10:])
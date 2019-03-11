year = 1901
count = 0
day = 2
start = 2

months=[31,28,31,30,31,30,31,31,30,31,30,31]
days,n=0,0
for i in range(0,101):
    if (not (1900+i)%4 and (1900+i)%100) or not (1900+i)%400: months[1]=29
    else: months[1]=28
    for t in months:
        if (days-1)%7==0 and i>=1:
            n+=1
        days+=t
print(n)

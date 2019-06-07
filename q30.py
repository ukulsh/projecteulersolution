i=2
TotalSum=0
while True:
    Sum=0
    for x in str(i): Sum+=int(x)**5
    if Sum==i: TotalSum+=Sum
    i+=1
if i>=354294:
        print(TotalSum)
previous = 1
current = 1
count = 1
while 1:
    fibo = previous+current
    previous = current
    current = fibo
    count+=1
    if len(str(fibo)) == 3:
        print(count+1)
        break

 
diagonalsum = 0
for i in range(2,1002):
    if i%2 != 0:
        temp = i**2
        diagonalsum += temp
        temp -= i-1
        print(temp)
        diagonalsum += temp
        temp -= i-1
        print(temp)
        
        diagonalsum += temp
        temp -= i-1
        print(temp)

        diagonalsum += temp 
print(diagonalsum+1)
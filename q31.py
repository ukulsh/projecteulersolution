def count(S, m, n ):  
    if (n == 0): 
        return 1
    if (n < 0): 
        return 0; 
    if (m <=0 and n >= 1): 
        return 0
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] ); 
arr = [1,2,5,10,20,50,100,200]
m = 8
n = 200
print(count(arr,8,200))
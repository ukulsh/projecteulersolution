arr = []
for arr_i in range(15):
    arr_temp = map(int,input().strip().split(' '))
    arr.append(list(arr_temp))
print(arr,'\n')
for i in range(13,-1,-1):
    for j in range(len(arr[i])):
        arr[i][j] += max(arr[i+1][j],arr[i+1][j+1])
print(arr[0][0])


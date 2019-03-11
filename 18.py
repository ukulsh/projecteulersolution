arr = []
arr.append(list(map(int,input().split())))
for i in range(14,0,-1):
    for j in range(len(arr[i])):
        if arr[i+1][j] > arr[i+1][j+1]:
            arr[i][j] = arr[i+1][j]
        else:
            arr[i][j] = arr[i+1][j+1]
print(arr[0][0])
with open('names.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

data = data.split(" ")

data = sorted(data)
print(data)
count = 1
arr = [0]*(len(data)+1)
for string in data:
    summ = 0
    for i in string:
        summ+=(ord(i)-64)
    summ = summ*count
    arr[count] = summ
    count+=1
print(sum(arr))
# summ = 0
# print(data[0],'\n')
# for i in data[0]:
#     summ=(ord(i)-64)
#     print(summ)


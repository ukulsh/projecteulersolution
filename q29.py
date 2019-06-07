sett = set()
for i in range(2,101):
    for j in range(2,101):
        sett.add(i**j)
print(len(sett))

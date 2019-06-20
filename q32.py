ans = set()
for k in range(1, 10000):
	for i in range(1,int(k**0.5) + 1):
		if k % i == 0:
			temp = str(k) + str(i) + str(k // i)
			if "".join(sorted(temp)) == "123456789":
				ans.add(k)
print(sum(ans))
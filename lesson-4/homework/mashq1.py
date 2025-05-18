list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

res = []
for i in list1:
	if i in list2:
		continue
	else:
		res.append(i)
print(res)
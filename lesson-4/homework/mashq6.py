def isPrime(a):
	j = int(a**(1/2))
	if j*j==a:return 0
	for i in range(2,j+1):
		if a%i==0:
			return 0
	return 1
for i in range(1,101):
	if isPrime(i):print(i)
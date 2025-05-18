def is_prime(n):
	if n==2:return True
	j= int(n**(1/2))
	if j*j==n:return False
	for i in range(3,j+1,2):
		if n%i==0:return False
	return True
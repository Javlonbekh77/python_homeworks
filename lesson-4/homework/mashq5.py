
while True:
	password = input("Input your strong password!!! ")
	if len(password)<8:
		print("Password is too short ")
	else:
		ok = False
		for i in password:
			if i.upper() == i:
				ok =True
				break
		if ok:
			print("Password is very Strong!!!")
			break
		else:
			print("Password must contain an uppercase letter.")
	print("Try Again .... ")
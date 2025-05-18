def invest(amount,rate,years):
	for i in range(years):
		amount = float(f"{amount*(rate/100)+amount:.2f}")
		print(f"years {i+1}: ${amount}")
invest(100,5,4)
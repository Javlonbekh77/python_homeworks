
def convert_cel_to_far():
	F = int(input("Enter a temperature in degrees F: "))
	C=f"{(F-32)*(5/9):.2f}"
	print(f"{F} degrees F={C} degrees C")
def convert_far_to_cel():
	C = int(input("Enter a temperature in degrees C: "))
	F=f"{C*(9/5)+32:.2f}"
	print(f"{C} degrees C={F} degrees F")


convert_cel_to_far()
convert_far_to_cel()
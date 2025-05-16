
d = eval(input("Enter dictionary: "))
inverted = {v: k for k, v in d.items()}
print(inverted)


d = eval(input("Enter dictionary: "))
value = input("Enter value to search for: ")
keys = [k for k, v in d.items() if v == value]
print(keys)

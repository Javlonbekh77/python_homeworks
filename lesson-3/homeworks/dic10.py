
d = eval(input("Enter dictionary: "))
key = input("Enter key: ")
if key in d:
    print((key, d[key]))
else:
    print("Key not found")

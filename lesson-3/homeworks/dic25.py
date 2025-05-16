
d = eval(input("Enter dictionary: "))
print(next(iter(d.items())) if d else "Dictionary is empty")

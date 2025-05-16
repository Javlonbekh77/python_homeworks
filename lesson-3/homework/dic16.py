
d = eval(input("Enter dictionary: "))
print(any(isinstance(v, dict) for v in d.values()))

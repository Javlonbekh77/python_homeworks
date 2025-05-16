
d = eval(input("Enter dictionary: "))
threshold = int(input("Enter threshold: "))
filtered = {k: v for k, v in d.items() if isinstance(v, int) and v >= threshold}
print(filtered)

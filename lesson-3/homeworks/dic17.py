
d = eval(input("Enter nested dictionary: "))
outer_key = input("Enter outer key: ")
inner_key = input("Enter inner key: ")
print(d.get(outer_key, {}).get(inner_key, "Key not found"))

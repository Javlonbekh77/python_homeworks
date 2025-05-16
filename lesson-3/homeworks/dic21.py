# 
d = eval(input("Enter dictionary: "))
print(dict(sorted(d.items(), key=lambda item: item[1])))

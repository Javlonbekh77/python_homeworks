
d1 = eval(input("Enter first dictionary: "))
d2 = eval(input("Enter second dictionary: "))
print(not d1.keys().isdisjoint(d2.keys()))

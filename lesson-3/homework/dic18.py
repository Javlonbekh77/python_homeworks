
from collections import defaultdict
default_value = input("Enter default value: ")
d = defaultdict(lambda: default_value)
print(d[input("Enter key: ")])

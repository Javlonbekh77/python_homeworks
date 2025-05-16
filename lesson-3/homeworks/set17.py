# Filter Odd Numbers
s = set(map(int, input("Enter integers separated by space: ").split()))
odd_set = {x for x in s if x % 2 != 0}
print("Odd numbers:", odd_set)
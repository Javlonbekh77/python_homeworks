# Filter Even Numbers
s = set(map(int, input("Enter integers separated by space: ").split()))
even_set = {x for x in s if x % 2 == 0}
print("Even numbers:", even_set)
s = input("So‘z kiriting: ").lower()
vowels = "aeiou"
v = sum(1 for c in s if c in vowels)
c = sum(1 for c in s if c.isalpha() and c not in vowels)
print(f"Unlilar: {v}, Undoshlar: {c}")
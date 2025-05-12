s = input("Matn kiriting: ")
print("Raqam bor." if any(c.isdigit() for c in s) else "Raqam yo‘q.")
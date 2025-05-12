s = input("Matn kiriting: ")
vowels = "aeiouAEIOU"
for v in vowels:
    s = s.replace(v, "*")
print(s)
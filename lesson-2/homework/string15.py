sentence = input("Gapni kiriting: ")
acronym = ''.join(word[0].upper() for word in sentence.split())
print("Acronym:", acronym)
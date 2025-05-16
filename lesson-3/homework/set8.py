# Remove Element
s = set(input("Enter elements of the set separated by space: ").split())
element = input("Enter element to remove: ")
s.discard(element)
print("Updated set:", s)
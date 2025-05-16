# Difference of Sets
set1 = set(input("Enter elements of first set separated by space: ").split())
set2 = set(input("Enter elements of second set separated by space: ").split())
difference_set = set1.difference(set2)
print("Difference:", difference_set)
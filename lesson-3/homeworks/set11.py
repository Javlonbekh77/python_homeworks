# Symmetric Difference
set1 = set(input("Enter elements of first set separated by space: ").split())
set2 = set(input("Enter elements of second set separated by space: ").split())
symmetric_diff = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_diff)
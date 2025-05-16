# Check Disjoint Sets
set1 = set(input("Enter elements of first set separated by space: ").split())
set2 = set(input("Enter elements of second set separated by space: ").split())
print("Are disjoint:", set1.isdisjoint(set2))
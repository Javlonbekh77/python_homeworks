# Check Subset
set1 = set(input("Enter elements of first set separated by space: ").split())
set2 = set(input("Enter elements of second set separated by space: ").split())
print("Is first set subset of second?", set1.issubset(set2))
print("Is second set subset of first?", set2.issubset(set1))
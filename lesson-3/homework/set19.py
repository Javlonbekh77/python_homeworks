# Merge and Deduplicate
list1 = input("Enter elements of first list separated by space: ").split()
list2 = input("Enter elements of second list separated by space: ").split()
merged_set = set(list1 + list2)
print("Merged set:", merged_set)
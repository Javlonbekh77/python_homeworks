# Pop Element
s = set(input("Enter elements of the set separated by space: ").split())
if s:
    popped = s.pop()
    print("Popped element:", popped)
else:
    print("Set is empty")
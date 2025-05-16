lst = list(input().split())
sublist = list(input().split())
found = False
for i in range(len(lst) - len(sublist) + 1):
    if lst[i:i+len(sublist)] == sublist:
        found = True
        break
print(found)
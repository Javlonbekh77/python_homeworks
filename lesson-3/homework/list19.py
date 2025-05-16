lst = list(input().split())
old = input()
new = input()
if old in lst:
    lst[lst.index(old)] = new
print(lst)
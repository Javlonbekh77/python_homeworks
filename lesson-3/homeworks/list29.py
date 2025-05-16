lst = list(input().split())
index = int(input())
if 0 <= index < len(lst):
    lst.pop(index)
print(lst)
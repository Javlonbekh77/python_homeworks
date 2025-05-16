lst = list(input().split())
element = input()
indices = [i for i, x in enumerate(lst) if x == element]
print(indices)
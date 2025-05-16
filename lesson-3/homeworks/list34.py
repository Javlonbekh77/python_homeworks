lst = list(input().split())
k = int(input())
k %= len(lst)
rotated = lst[-k:] + lst[:-k]
print(rotated)
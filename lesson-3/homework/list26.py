lst = list(input().split())
n = len(lst)
if n % 2 == 0:
    print(lst[n//2 - 1], lst[n//2])
else:
    print(lst[n//2])
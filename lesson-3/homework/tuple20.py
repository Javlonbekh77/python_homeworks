t = tuple(input().split())
n = int(input())
nested = tuple(tuple(t[i:i+n]) for i in range(0, len(t), n))
print(nested)
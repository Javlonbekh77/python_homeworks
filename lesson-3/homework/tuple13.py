t = tuple(map(int, input().split()))
print(sorted(set(t))[1] if len(set(t)) >= 2 else None)
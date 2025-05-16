t = tuple(input().split())
seen = set()
unique = tuple(x for x in t if not (x in seen or seen.add(x)))
print(unique)
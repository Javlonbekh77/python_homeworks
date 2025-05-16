lst = list(input().split())
seen = set()
unique_ordered = []
for x in lst:
    if x not in seen:
        seen.add(x)
        unique_ordered.append(x)
print(unique_ordered)
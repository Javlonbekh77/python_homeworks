t = tuple(input().split())
n = int(input())
print(tuple(x for x in t for _ in range(n)))
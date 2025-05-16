t = tuple(map(int, input().split()))
start, end = map(int, input().split())
print(min(t[start:end]))
t = tuple(map(int, input().split()))
start, end = map(int, input().split())
print(max(t[start:end]))
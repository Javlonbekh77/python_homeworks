lst = list(input().split())
n = int(input())
nested = [lst[i:i+n] for i in range(0, len(lst), n)]
print(nested)
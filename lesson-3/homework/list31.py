lst = list(input().split())
n = int(input())
result = [x for x in lst for _ in range(n)]
print(result)
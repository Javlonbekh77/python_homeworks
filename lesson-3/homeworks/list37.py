lst = list(map(int, input().split()))
print(sum(x for x in lst if x < 0))
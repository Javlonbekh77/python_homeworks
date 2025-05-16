lst = list(map(int, input().split()))
odd_lst = [x for x in lst if x % 2 != 0]
print(odd_lst)
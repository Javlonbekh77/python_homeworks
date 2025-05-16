t = tuple(map(int, input().split()))
print(all(t[i] <= t[i+1] for i in range(len(t)-1)))
# Generate Random Set
import random
count = int(input("Enter number of random integers: "))
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
random_set = set()
while len(random_set) < count:
    random_set.add(random.randint(start, end))
print("Random set:", random_set)
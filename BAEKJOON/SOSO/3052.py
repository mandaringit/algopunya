rest_set = set()
for _ in range(10):
    number = int(input())
    rest = number % 42
    rest_set.add(rest)
print(len(rest_set))

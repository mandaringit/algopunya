N, X = tuple(map(int, input().split()))
A = list(map(int, input().split()))
result = ""
for num in A:
    if num < X:
        result += str(num) + " "
print(result.rstrip())

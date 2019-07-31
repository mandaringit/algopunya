T = int(input())
for _ in range(T):
    num, word = input().split()
    result = ""
    for char in word:
        result += char*int(num)
    print(result)

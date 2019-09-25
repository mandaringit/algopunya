import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    word = input()

    N = len(word)

    center = N // 2
    is_palindrome = 1
    for i in range(0, center):
        if word[i] != word[N - 1 - i]:
            is_palindrome = 0

    print(f"#{tc} {is_palindrome}")


# print(1) if word == word[::-1] else print(0)
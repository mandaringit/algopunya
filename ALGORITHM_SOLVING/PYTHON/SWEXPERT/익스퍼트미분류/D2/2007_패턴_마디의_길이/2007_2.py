import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    words = input()

    first_char = words[0]

    for i in range(1, len(words) - 1):
        if words[i] == first_char:
            repeat_word = words[:i]

            if repeat_word == words[i:i + len(repeat_word)]:
                print(f"#{tc} {len(repeat_word)}")
                break

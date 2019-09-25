# 그룹단어
def isGroupWord(word):
    pick_word = word[0]
    already_used = set()

    for idx, char in enumerate(word):
        if char in already_used:
            return False
        else:
            if char != pick_word:
                already_used.add(pick_word)
                pick_word = char

            if idx == len(word)-1:
                return True


T = int(input())
count = 0
for _ in range(T):
    word = input()
    if isGroupWord(word):
        count += 1
print(count)

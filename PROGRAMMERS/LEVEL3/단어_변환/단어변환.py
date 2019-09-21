begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]


def solution(begin, target, words):
    N = len(begin)

    # BFS 탐색
    visited = set()
    possible_words = set(words)

    q = [[begin, 0]]

    while q:
        word, count = q.pop(0)

        if word == target:
            return count
        else:
            for nv_word in possible_words:
                same_count = 0
                for i in range(N):
                    if nv_word[i] != word[i]:
                        same_count += 1
                        if same_count > 1:
                            break

                if same_count == 1:
                    if nv_word == target:
                        return count + 1
                    else:
                        visited.add(nv_word)
                        q.append([nv_word, count + 1])

            possible_words -= visited

    return 0


print(solution(begin, target, words))

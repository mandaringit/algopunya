import sys

sys.stdin = open('sample_input.txt', 'r')


def shuffle(x, cards, N):
    half = N // 2
    left = cards[:half]
    right = cards[half:]

    if x < N // 2:
        l = left[:half - x]
        r = right[x:]
        middle = list(zip(right[:x], left[half - x:half]))

        shuffled = [*l]

        for i, j in middle:
            shuffled.append(i)
            shuffled.append(j)

        shuffled += r

        return shuffled

    else:
        x = N - 1 - x
        l = right[:half - x]
        r = left[x:]
        middle = list(zip(left[:x], right[half - x:half]))

        shuffled = [*l]

        for i, j in middle:
            shuffled.append(i)
            shuffled.append(j)

        shuffled += r

        return shuffled


# 방문여부를 체크할 필요가 없다 ? in 을 쓰면서 속도가 엄청나게 느려진다.
def BFS(start, N):
    asc = sorted(start)
    dec = list(reversed(asc))

    q = [(start, 0)]
    # visited = []
    while q:
        cards, depth = q.pop(0)
        # visited.append(cards)
        if depth > 5:
            return -1

        if cards == asc or cards == dec:
            return depth

        for i in range(1, N):
            shuffled = shuffle(i, cards, N)
            n_depth = depth + 1

            if shuffled == asc or shuffled == dec:
                return n_depth

            if n_depth < 5:
                q.append((shuffled, n_depth))
                # visited.append(cards)

    return -1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    cards = list(map(int, input().split()))

    print("#{} {}".format(tc, BFS(cards, N)))

import sys

sys.stdin = open('input.txt', 'r')


def get_kevin_number(i, j):
    global friendships
    global kevin_numbers

    q = [(i, {i})]

    while q:
        node, visited = q.pop(0)

        for friend in friendships[node] - visited:
            next_visited = visited | {friend}
            if friend == j:
                kevin_numbers[i] += (len(next_visited) - 1)
                return
            else:
                q.append((friend, next_visited))


N, M = map(int, input().split())

friendships = {i: set() for i in range(1, N + 1)}

for _ in range(M):
    f1, f2 = map(int, input().split())

    friendships[f1].add(f2)
    friendships[f2].add(f1)

kevin_numbers = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j != i:
            get_kevin_number(i, j)

print(kevin_numbers[1:].index(min(kevin_numbers[1:])) + 1)

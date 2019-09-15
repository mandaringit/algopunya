import sys

sys.stdin = open('input.txt', 'r')

# BFS로도 풀어보삼

while True:

    line = input()

    if line == '0':
        break

    else:
        info = list(map(int, line.split()))

        N = info[0]

        numbers = info[1:]

        subsets = []

        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    for l in range(k + 1, N):
                        for m in range(l + 1, N):
                            for n in range(m + 1, N):
                                subset = [numbers[i], numbers[j], numbers[k], numbers[l], numbers[m], numbers[n]]

                                subsets.append(subset)

        for subset in subsets:
            print(' '.join(map(str, subset)))
    print()

import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

numbers = [number for number in range(1, N + 1)]
all_seq = []
for i in range(N):
    q = [[numbers[i]]]

    while q:
        seq = q.pop(0)

        if len(seq) == M:
            all_seq.append(seq)
        else:
            for num in numbers:
                if num not in seq:
                    new_seq = seq + [num]
                    q.append(new_seq)

for seq in all_seq:
    print('{}'.format(' '.join(map(str, seq))))

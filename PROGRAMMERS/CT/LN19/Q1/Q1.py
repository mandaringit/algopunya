import sys

sys.stdin = open('input.txt', 'r')

M, C = map(int, input().strip().split())

messages = [int(input().strip()) for _ in range(M)]
consumers = [[] for _ in range(C)]

for m_size in messages:

    min_len = len(consumers[0])
    consumer_idx = 0

    for i in range(C):
        consumer = consumers[i]
        length = len(consumer)
        if length < min_len:
            min_len = len(consumer)
            consumer_idx = i

    consumers[consumer_idx] += [1] * m_size

max_time = 0
for consumer in consumers:
    if len(consumer) > max_time:
        max_time = len(consumer)
print(consumers)
print(max_time)

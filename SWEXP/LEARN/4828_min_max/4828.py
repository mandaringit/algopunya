import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split()))

    max_number = 0
    min_number = 1000000

    for i in range(0, N):
        if numbers[i] > max_number:
            max_number = numbers[i]

        if numbers[i] < min_number:
            min_number = numbers[i]

    print(f"#{tc} {max_number - min_number}")

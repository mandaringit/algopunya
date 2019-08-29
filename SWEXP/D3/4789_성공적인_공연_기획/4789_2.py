import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    wakeups = list(map(int, list(input())))

    im_wake = 0
    employ = 0
    for i in range(0, len(wakeups)):

        # i => 일어나는데 필요한 사람 수

        if im_wake >= i:
            im_wake += wakeups[i]

        else:
            need = i - im_wake
            im_wake += need
            employ += need
            im_wake += wakeups[i]

    print("#{} {}".format(tc, employ))

import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    num_2 = input()
    num_3 = input()

    base2 = []
    for i in range(len(num_2)):

        if num_2[i] == '0':
            assume = num_2[:i] + '1' + num_2[i + 1:]
        else:
            assume = num_2[:i] + '0' + num_2[i + 1:]

        base2.append(assume)

    base3 = []
    for i in range(len(num_3)):

        if num_3[i] == '0':
            assume1 = num_3[:i] + '1' + num_3[i + 1:]
            assume2 = num_3[:i] + '2' + num_3[i + 1:]
        elif num_3[i] == '1':
            assume1 = num_3[:i] + '0' + num_3[i + 1:]
            assume2 = num_3[:i] + '2' + num_3[i + 1:]
        else:
            assume1 = num_3[:i] + '0' + num_3[i + 1:]
            assume2 = num_3[:i] + '1' + num_3[i + 1:]

        base3.append(assume1)
        base3.append(assume2)

    base2_decimals = set()
    base3_decimals = set()

    for binary in base2:
        base2_decimals.add(int(binary, 2))

    for three in base3:
        base3_decimals.add(int(three, 3))

    print("#{} {}".format(tc, list(base2_decimals & base3_decimals)[0]))

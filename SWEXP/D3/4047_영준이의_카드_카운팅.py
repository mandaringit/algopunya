def card_distribution(cases):
    card_pack = {
        'S': [],
        'D': [],
        'H': [],
        'C': []
    }

    for i in range(0, len(cases), 3):
        case = cases[i:i + 3]

        pattern = case[0]
        number = int(case[1:])

        if number in card_pack[pattern]:
            return 'ERROR'
        else:
            card_pack[pattern].append(number)

    lack_card_count = ''
    for i in ['S', 'D', 'H', 'C']:
        lack_card_count += f"{13 - len(card_pack[i])} "

    return lack_card_count


T = int(input())

for tc in range(1, T + 1):
    cases = input()

    result = card_distribution(cases)

    print(f"#{tc} {result}")

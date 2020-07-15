T = int(input())

for tc in range(1, T + 1):
    word = input()

    line1 = ""
    line2 = ""
    line3 = ""

    for i in range(0, len(word)):
        pattern1 = "..#.."
        pattern2 = ".#.#."
        pattern3 = f"#.{word[i]}.#"

        if i == 0:
            line1 += pattern1
            line2 += pattern2
            line3 += pattern3
        else:
            # 이후부터는 맨 앞줄만 삭제하고 집어넣으면 된다.
            line1 += pattern1[1:]
            line2 += pattern2[1:]
            line3 += pattern3[1:]

    print(line1)
    print(line2)
    print(line3)
    print(line2)
    print(line1)

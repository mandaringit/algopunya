from collections import defaultdict


def defaultdict_example():
    pairs = {("a", 1), ("b", 2), ("c", 3)}

    d1 = {}
    for key, value in pairs:
        if key not in d1:
            d1[key] = []
        d1[key].append(value)

    print(d1)

    # default dict
    # 누락된 키도 처리 가능하다.
    d2 = defaultdict(list)
    for key, value in pairs:
        d2[key].append(value)
    print(d2)


if __name__ == "__main__":
    defaultdict_example()

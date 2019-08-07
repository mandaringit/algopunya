# 아직 통과 못함
# 50개중 8개


def addIn(x, y, dict_storage):
    if x in dict_storage:
        dict_storage[x].append(y)
    else:
        dict_storage[x] = [y]

    if y in dict_storage:
        dict_storage[y].append(x)
    else:
        dict_storage[y] = [x]

    return dict_storage


def getTriangleCount(case_dict):
    triangle_cases = []

    for edge, nodes in case_dict.items():
        for idx, node in enumerate(nodes):
            if idx == len(nodes) - 1:
                continue
            else:
                pick1 = node
                pick2 = nodes[idx + 1]
                try_case = {edge, pick1, pick2}
                if try_case not in triangle_cases:
                    if pick1 in case_dict[pick2] and pick2 in case_dict[pick1]:
                        triangle_cases.append(try_case)
    return len(triangle_cases)


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())

    case_dict = {}

    for m in range(1, M + 1):
        x, y = map(int, input().split())

        case_dict = addIn(x, y, case_dict)

    triangle_count = getTriangleCount(case_dict)

    print(f"#{t} {triangle_count}")

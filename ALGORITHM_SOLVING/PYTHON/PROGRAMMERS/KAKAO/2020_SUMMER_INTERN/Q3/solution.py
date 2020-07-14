"""
# 시간초과
# 정확도 통과
Q3
# 입력


# 출력

# 접근
    - 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 "가장 짧은 구간"을 찾아서 구매

"""


def solution(gems):
    total_length = len(set(gems))
    results = {}

    smallest_length = len(gems)
    sequences = []

    for idx, gem in enumerate(gems):
        number = idx + 1
        results[number] = set()
        results[number].add(gem)

        for i in range(1, number + 1):
            results[i].add(gem)
            seq_len = number - i
            # 다 모였고,
            if len(results[i]) == total_length:
                #  길이가 현재랑 같다면
                if seq_len == smallest_length:
                    sequences.append([i, number])
                elif seq_len < smallest_length:
                    sequences = [[i, number]]
                    smallest_length = seq_len

    return sequences[0]


solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
solution(["XYZ", "XYZ", "XYZ"])

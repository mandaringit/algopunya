import sys

sys.stdin = open('input.txt', 'r')


def solution(s):
    filtered = s.lstrip("{{").rstrip("}}").split("},{")
    tuples = [tuple(map(int, sets.split(","))) for sets in filtered]
    tuples.sort(key=lambda x: len(x))

    result_tuple = [*tuples[0]]

    for tup in tuples[1:]:
        for el in tup:
            if el not in result_tuple:
                result_tuple.append(el)

    return result_tuple

solution("{{20,111},{111}}")
solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
solution("{{123}}")

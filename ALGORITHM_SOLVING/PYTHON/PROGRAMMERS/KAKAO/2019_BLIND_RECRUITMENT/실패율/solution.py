import unittest


def solution(N, stages):
    challenger = len(stages)
    not_clear = [0] * (N + 2)

    for stage in stages:
        not_clear[stage] += 1

    # 실패율을 구한다.
    fail_rate = {}
    for i in range(1, N + 1):
        if challenger != 0:
            rate = not_clear[i] / challenger
        else:
            rate = 0
        fail_rate[i] = rate
        challenger -= not_clear[i]

    # 실패율을 내림차순으로 정렬한다.
    # items()는 key, value를 리턴, 그중 [1]번째 인덱스인 value를 통해 정렬한다.
    sorted_fail_rate = sorted(fail_rate.items(), key=lambda item: item[1], reverse=True)
    return [sorted_fail_rate[i][0] for i in range(N)]


class MyTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]), [3, 4, 2, 1, 5])

    def test_case2(self):
        self.assertEqual(solution(4, [4, 4, 4, 4, 4]), [4, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()

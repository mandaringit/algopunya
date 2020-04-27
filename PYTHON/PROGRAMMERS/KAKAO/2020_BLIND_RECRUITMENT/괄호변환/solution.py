def solution(p):
    # 균형잡힌 괄호 문자열? == ( ) 갯수 같은거
    def is_balanced(brackets):
        bracket_count = {
            '(': 0,
            ')': 0
        }

        for bracket in brackets:
            bracket_count[bracket] += 1

        return bracket_count['('] == bracket_count[')']

    # 올바른 괄호 문자열?
    def is_right(brackets):
        stack = []
        for bracket in brackets:
            if len(stack) == 0:
                stack.append(bracket)
            else:
                recent_bracket = stack[-1]
                if recent_bracket == '(' and bracket == ')':
                    stack.pop()
                else:
                    stack.append(bracket)
        return len(stack) == 0

    # 분리
    def separate(brackets):
        if brackets == '':
            return ''
        elif is_balanced(brackets) and is_right(brackets):
            return brackets
        else:
            # 2. 두 "균형잡힌 괄호 문자열" u, v로 분리한다.
            for i in range(1, len(brackets) + 1):
                u = brackets[:i]  # 더이상 분리 불가
                v = brackets[i:]  # 빈 문자열 가능

                # 둘 다 균형잡힌 괄호 문자열일 때만 시도
                if is_balanced(u) and is_balanced(v):
                    if is_right(u):
                        return u + separate(v)
                        # 수행한 결과 문자열을 u에 붙힌 후 반환한다.
                    else:
                        result = "(" + separate(v) + ")"
                        # u의 첫 번째와 마지막 문자를 제거하고
                        last = u[1:-1]

                        # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
                        for bracket in last:
                            if bracket == "(":
                                result += ")"
                            elif bracket == ")":
                                result += "("

                        return result

    return separate(p)


import unittest


class MyTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solution("(()())()"), "(()())()")

    def test_case2(self):
        self.assertEqual(solution(")("), "()")

    def test_case3(self):
        self.assertEqual(solution("()))((()"), "()(())()")


if __name__ == '__main__':
    unittest.main()

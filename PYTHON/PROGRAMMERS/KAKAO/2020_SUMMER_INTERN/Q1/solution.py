"""
Q1
# 입력
    순서대로 누를 번호가 담긴 배열 numbers
    왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand

# 출력
    각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return

# 접근
    1. 왼손, 오른손 최초 위치에서 시작,
    2. 1,4,7은 무조건 왼손 이동
    3. 3,6,9는 무조건 오른손 이동
    4. 중간번호들은 현재 손가락과 번호의 거리 비교후 가까운거 우선
    5. 거리가 동일하다면 => hand 고려
    6. 누른 손 저장
"""


def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    keypad_loc = {}

    # 키패드 위치 저장
    for i in range(4):
        for j in range(3):
            keypad_loc[keypad[i][j]] = (i, j)

    # 왼손 오른손 최초 위치 시작
    left = '*'
    right = '#'

    for touch_number in numbers:
        if touch_number in [1, 4, 7]:
            answer += 'L'
            left = touch_number
        elif touch_number in [3, 6, 9]:
            answer += 'R'
            right = touch_number
        else:
            ti, tj = keypad_loc[touch_number]
            li, lj = keypad_loc[left]
            ri, rj = keypad_loc[right]
            left_d = abs(ti - li) + abs(tj - lj)
            right_d = abs(ti - ri) + abs(tj - rj)

            if left_d < right_d:
                answer += "L"
                left = touch_number
            elif left_d > right_d:
                answer += "R"
                right = touch_number
            else:
                if hand == "left":
                    answer += "L"
                    left = touch_number
                else:
                    answer += "R"
                    right = touch_number

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))

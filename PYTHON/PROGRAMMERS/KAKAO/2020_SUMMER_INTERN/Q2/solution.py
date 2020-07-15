"""
Q2
- 숫자들 + 연산자들
- 같은 순위의 연산자는 없어야 한다. => 무조건 각자 순서가 있어야됨

# 입력

# 출력
    - 연산자 자유롭게 재정의하여 만들 수 있는 가장 큰 숫자
# 접근
    1. 연산자의 우선순위를 만들 수 있는 방법을 모두 만든다.
    2. 해당 연산자 순서를 고려한 계산 실시 => + - * 으로 split ? (음수단위 없음)
    3. 음수 결과면 절대값 씌우기
    4. 결과 비교
"""


def solution(expression):
    numbers = []
    ops = []
    num = ''
    for idx, char in enumerate(expression):

        if char.isdigit():
            num += char
        else:
            numbers.append(int(num))
            num = ''
            ops.append(char)

        if idx == len(expression) - 1:
            numbers.append(int(num))

    # 2. 해당 연산자 순서를 고려한 계산 실시 => + - * 으로 split ? (음수단위 없음)
    print(numbers, ops)

    # 3. 음수 결과면 절대값 씌우기

    # 4. 결과 비교

    return ''


solution("100-200*300-500+20")  # 60240
solution("50*6-3*2")  # 300

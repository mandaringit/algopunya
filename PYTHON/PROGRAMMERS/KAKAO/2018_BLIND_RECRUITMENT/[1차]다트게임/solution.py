def solution(dartResult):
    results = ['', '', '']
    scores = [0, 0, 0]
    stage = 0

    # 먼저 각 스테이지별로 나눈다
    for char in dartResult:
        if char in 'SDT':  # 숫자면 스테이지 1 업
            results[stage] = results[stage] + char
            stage += 1
        elif char in '#*':
            results[stage - 1] = results[stage - 1] + char
        else:
            results[stage] = results[stage] + char

    areas = {
        'S': 1,
        'D': 2,
        'T': 3,
    }

    # 각 스테이지별로 점수 계산
    for idx, result in enumerate(results):
        basic_score = ''
        area = ''
        option = None
        for char in result:
            if char.isdigit():
                basic_score += char
            elif char in 'SDT':
                area = char
            else:
                option = char

        scores[idx] = int(basic_score) ** areas[area]

        if option:
            if option == '*':
                if idx > 0:
                    scores[idx - 1] = scores[idx - 1] * 2
                scores[idx] = scores[idx] * 2
            elif option == '#':
                scores[idx] = -scores[idx]

    return sum(scores)


solution('1S2D*3T')

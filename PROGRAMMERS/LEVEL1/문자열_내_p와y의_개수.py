def solution(s):

    p_count = y_count = 0

    for char in s.lower():
        if char == 'p':
            p_count += 1
        elif char == 'y':
            y_count += 1

    return p_count == y_count


solution("pPooy")
solution("Pyy")

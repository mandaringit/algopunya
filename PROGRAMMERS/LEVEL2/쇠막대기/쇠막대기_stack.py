def solution(arrangement):
    stack = [arrangement[0]]
    prev = stack[0]
    bar_count = 0
    cutting_bar = 0
    for bracket in arrangement[1:]:
        # 레이저일때
        if prev == '(' and bracket == ')':
            cutting_bar += bar_count
            stack.pop()
        elif prev == '(' and bracket == '(':
            bar_count += 1
            cutting_bar += 1
            stack.append(bracket)
        elif prev == ')' and bracket == '(':
            stack.append(bracket)
        elif prev == ')' and bracket == ')':
            stack.pop()
            bar_count -= 1
        prev = bracket
    return cutting_bar


solution("()(((()())(())()))(())")

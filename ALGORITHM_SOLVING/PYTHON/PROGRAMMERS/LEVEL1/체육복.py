
def solution(n, lost, reserve):
    answer = 0

    # 여벌중 도난인사람 제외
    Students = list(range(1, n+1))  # 전체 학생
    Lost = list(set(lost) - set(reserve))  # 잃어버린 사람 : 잃음 - 여벌
    Reserve = list(set(reserve) - set(lost))  # 여벌 : 여벌 - 잃음

    # 빌려주기
    for number in Lost:
        if number - 1 in Reserve:
            Reserve.remove(number-1)
        elif number + 1 in Reserve:
            Reserve.remove(number+1)
        else:
            # 둘다 아닐때 수업가능 학생에서 제외
            Students.remove(number)

    # 전체 수 - len(lost) = 수업가능 수
    answer = len(Students)

    return answer


print(solution(5, [2, 4], [1, 3, 5]))  # 5
print(solution(5, [2, 4], [3]))  # 4
print(solution(3, [3], [1]))  # 2
print(solution(5, [2, 3, 4], [3]))  # 3
print(solution(5, [2, 3, 4], [3, 4, 5]))  # 4


# 1차
# 1,3,5 실패
# 루프도는걸 중간에 삭제하고있었음
"""
def solution(n, lost, reserve):
    answer = 0

    # 여벌 중, 도난이 있는지 확인하고 제외
    for number in reserve:
        if number in lost:
            # 도난된 친구는 여벌이 없다고 봄
            reserve.remove(number)  ######## 테케실패의 원인 <= 멍청한짓. 루프도는걸 깎으면 안되지 ㅠㅠ
            # 여벌이 있으니 잃어버린것도 아님
            lost.remove(number)
    
    # 빌려주기
    for number in reserve:
        if number - 1 in lost:
            lost.remove(number - 1)
        elif number + 1 in lost:
            lost.remove(number + 1)
    
    # 전체 수 - len(lost) = 수업가능 수
    answer = n - len(lost)

    return answer


print(solution(5, [2, 4], [1, 3, 5]))  # 5
print(solution(5, [2, 4], [3]))  # 4
print(solution(3, [3], [1]))  # 2
print(solution(5, [2, 3, 4], [3])) # 3
print(solution(5, [2, 3, 4], [3,4,5])) # 4
"""

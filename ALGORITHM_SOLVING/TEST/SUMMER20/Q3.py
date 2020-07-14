def solution(total_sp, skills):
    skill_length = len(skills) + 2
    skill_dict = {i: [] for i in range(1, skill_length)}
    points = [0] * skill_length
    for a, b in skills:
        if a in skill_dict:
            skill_dict[a].append(b)

    def get_point(i):
        print(points)
        sum_p = 0
        if len(skill_dict[i]) == 0:
            points[i] = 1
            return 1
        else:
            for child in skill_dict[i]:
                if points[child] == 0:
                    sum_p += get_point(child)
                else:
                    sum_p += points[i]
            points[i] = sum_p
            return sum_p


    for i in range(1, skill_length):
        print(i)
        if points[i] == 0:
            get_point(i)
            print(points)

    ratio = int(total_sp / sum(points))
    skill_points = [point * ratio for point in points[1:]]
    return skill_points


solution(121, [[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]])

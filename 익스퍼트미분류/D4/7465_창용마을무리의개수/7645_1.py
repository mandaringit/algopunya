def checkGroup(person_set, groups):
    # 나중에 포함되는 그룹을 묶기 위해 각 인덱스를 모아준다.
    idxs = []

    for idx, group in enumerate(groups):
        # 일단 각 그룹을 돌면서 교차하는게 있으면 그룹을 업데이트
        if len(person_set & group) > 0:
            # 인덱스도 idxs에 추가
            idxs.append(idx)
            # 기존 그룹은 합친걸로 교체
            groups[idx] = group | person_set

    # 예로,
    # 초기엔 {1,2} {4,5} 처럼 두개 그룹이다가 {2,4}를 넣고 난 이후에 겹치는 경우가 생김
    # 이후 겹치는게 두개 이상 인지 확인 => {1,2,4} {2,4,5} => 두개를 합쳐야함
    if len(idxs) > 1:

        # 새로운 그룹을 만들어서
        new_group = set()
        # 모아놓은 인덱스들을 거꾸로 돌면서 (앞에서부터 제거하면 인덱스순서가 달라지니까)
        for i in idxs[::-1]:
            # 새로운 그룹에 합치고
            new_group = new_group | groups[i]
            # 기존 그룹은 그룹들에서 제거
            groups.pop(i)

        # 새로합친 그룹을 그룹들에 추가
        groups.append(new_group)

    # 겹치는게 없을땐 단순하게 그룹들에 추가
    if not idxs:
        groups.append(person_set)

    return groups


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    groups = []

    # 모든 사람을 먼저 그룹에 넣자
    for p in range(1, N+1):
        groups.append({str(p)})

    # 케이스마다 그룹 체킹
    for _ in range(M):
        a, b = input().split()

        groups = checkGroup({a, b}, groups)

    print(f"#{t} {len(groups)}")

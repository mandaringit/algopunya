T = int(input())

for tc in range(1, T + 1):
    how_many_stand = list(map(int, input()))

    current_stand_up = 0
    total_employ = 0

    # 0 -> 끝까지 돈다
    # 해당 인덱스 = 요구 인원수
    for required_stand_up in range(0, len(how_many_stand)):

        # 부족시 미리 고용
        if required_stand_up > current_stand_up:
            # 부족한 수만큼 고용하고
            lack_stand_up = (required_stand_up - current_stand_up)
            current_stand_up += lack_stand_up
            # 총 고용자 수에 더해준다
            total_employ += lack_stand_up

        # 이제 고용을 했든 안했든 현재 기립박수자 수로 비교
        if required_stand_up <= current_stand_up:
            current_stand_up += how_many_stand[required_stand_up]

    print(f"#{tc} {total_employ}")

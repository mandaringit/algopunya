for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    total_good_view = 0

    for i in range(2, N - 2):

        building_h = buildings[i]
        near_buildings = [buildings[i + d] for d in [-2, -1, 1, 2]]

        near_top = 0

        for near_height in near_buildings:
            if near_height > near_top:
                near_top = near_height

        good_view_count = building_h - near_top if building_h > near_top else 0

        total_good_view += good_view_count

    print(f"#{tc} {total_good_view}")

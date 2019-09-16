import sys

sys.stdin = open("sample_input.txt", 'r')

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())  # 최대거리, 종점, 공급소 수

    e_stations = list(map(int, input().split()))  # 공급소 인덱스
    supply_count = 0
    stationIdx = 0
    possible_distance = K

    isPossible = True

    for i in range(M):
        # 마지막 주유소일땐
        if i == M - 1:
            # 충전해도 목적지까지 거리가 부족할때 (못감1)
            if N - e_stations[i] > K:
                isPossible = False
        # 주유소간 거리가 충전 후 이동거리보다 멀때 (못감2)
        elif e_stations[i + 1] - e_stations[i] > K:
            isPossible = False

    if isPossible:
        for current_location in range(1, N + 1):  # i는 현재 위치
            possible_distance -= 1

            # 충전소에 도달했을때 고민한다
            if current_location == e_stations[stationIdx]:

                # 충전소가 마지막인지 확인
                if stationIdx == M - 1:
                    # 1. 충전 안하고도 도착 가능한지
                    if possible_distance >= N - current_location:
                        break
                    # 2. 지금 상태론 못가지만 충전하면 가능 할때
                    elif possible_distance < N - current_location <= K:
                        supply_count += 1
                        break
                else:
                    # 충전소가 마지막이 아니면 다음 주유소까지 여유가 되는지 본다
                    if e_stations[stationIdx + 1] - current_location > possible_distance:
                        supply_count += 1  # 충전
                        possible_distance = K  # 거리상승
                        stationIdx += 1  # 다음 충전소로 인덱스 변경
                    else:
                        # 여유 되면 그냥 지나치자
                        stationIdx += 1  # 다음 충전소로 변경

    print(f"#{tc} {supply_count}")

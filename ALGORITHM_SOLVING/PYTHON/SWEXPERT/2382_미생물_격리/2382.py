import sys

sys.stdin = open('sample_input.txt', 'r')


class Micro:

    def __init__(self, x, y, count, direction, range):
        self.x = x  # 가로 위치
        self.y = y  # 세로 위치
        self.count = count  # 군집내 미생물 수
        self.direction = direction
        self.range = range
        self.dead = False

    # 자신의 방향을 전환시키는 메서드
    def change_direction(self):
        # 상 하 좌 우
        if self.direction == 1:
            self.direction = 2
        elif self.direction == 2:
            self.direction = 1
        elif self.direction == 3:
            self.direction = 4
        elif self.direction == 4:
            self.direction = 3

    # 자신의 미생물수를 절반으로
    def cutting_half_micro(self):
        self.count = self.count // 2
        if self.count == 0:
            self.dead = True

    def move(self):
        if self.direction == 1:
            self.x -= 1
        elif self.direction == 2:
            self.x += 1
        elif self.direction == 3:
            self.y -= 1
        elif self.direction == 4:
            self.y += 1

        # 화학약품에 들어갈때 행동
        if self.x == 0 or self.x == self.range - 1 or self.y == 0 or self.y == self.range - 1:
            self.change_direction()
            self.cutting_half_micro()

        return self.x, self.y  # 자신의 좌표 반환


# 한 셀에 모일때
def micro_meeting(micros):
    biggest_count = 0
    biggest_micro = micros[0]
    total_micro = 0

    # 가장 큰 미생물군집을 찾는 과정
    for micro in micros:
        total_micro += micro.count
        if micro.count > biggest_count:
            biggest_count = micro.count
            biggest_micro = micro

    # 가장 큰 미생물군집의 미생물 수는 이제 한셀에 모인 모든 미생물수의 합이 된다.
    biggest_micro.count = total_micro

    # 가장 큰 미생물을 제외하고 나머지 미생물은 사망
    for micro in micros:
        if micro != biggest_micro:
            micro.dead = True


T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    micros = []

    # 각 미생물 저장
    for _ in range(K):
        x, y, count, d = list(map(int, input().split()))
        micro = Micro(x, y, count, d, N)
        micros.append(micro)

    hour = 0
    while hour < M:
        hour += 1  # 1시간씩 직접 가보자

        locations = {}  # 좌표별로 한곳에 모이는 미생물을 모은다

        for micro in micros:
            if not micro.dead:  # 안죽은 놈들만 검사
                coordinate = micro.move()  # 이동 후 위치
                if coordinate in locations:
                    locations[coordinate].append(micro)
                else:
                    locations[coordinate] = [micro]

        #  각 좌표에 존재하는 미생물의 개수를 살펴보자
        for coordinate in locations:
            micro_group = locations[coordinate]
            if len(micro_group) >= 2:  # 한셀에 두개 이상 모이면
                micro_meeting(micro_group)  # 미팅을 가진다

    total_count = 0
    for micro in micros:
        if not micro.dead:
            total_count += micro.count

    print("#{} {}".format(tc, total_count))

import sys

sys.stdin = open('input.txt', 'r')


def get_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def delivery(x, y, distance, remain_customers):
    global customers
    global min_distance
    global home

    if not remain_customers:
        # 집까지 거리
        to_home_d = get_distance(*home, x, y)
        distance += to_home_d
        if distance < min_distance:
            min_distance = distance

    else:
        if distance < min_distance:
            for customer in list(remain_customers):
                nx, ny = customer
                d = get_distance(*customer, x, y)
                delivery(nx, ny, distance + d, remain_customers - {customer})


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    coord = list(map(int, input().split()))

    company = (coord[0], coord[1])
    home = (coord[2], coord[3])

    customers = set()
    deliverd = set()

    for i in range(4, len(coord) - 1, 2):
        customers.add((coord[i], coord[i + 1]))

    min_distance = 200 * len(customers)

    for customer in list(customers):
        distance = get_distance(*customer, *company)  # 회사 - > 첫번째 고객
        x, y = customer

        deliverd = {customer}
        # 고객 주소, 배달 거리, 남은 배달 장소 , 지금까지 간 배달 장소
        delivery(x, y, distance, customers - deliverd)  # 고객 -> 고객

    print("#{} {}".format(tc, min_distance))

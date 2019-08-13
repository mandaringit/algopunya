T = int(input())

for tc in range(1, T + 1):
    HM, DHB, money = map(int, input().split())

    # 어떤 빵이든 상관 없이 그냥 많은 개수의 빵을 사고싶다.
    # 두 종류의 개수를 다르게 사도 되고, 한종류만 사도 괜찮다.

    # 두 빵의 가격 비교
    cheap_price = DHB if HM >= DHB else HM
    expensive_price = DHB if cheap_price == HM else HM

    cheap_count = money // cheap_price
    expensive_count = 0
    last = money % cheap_price

    if last != 0 and cheap_price != expensive_price:
        cheap_count -= 1
        last += cheap_price

        # 한가지 경우밖에 없음? 나머지 + 싼가격 % 비싼가격 했을때
        # 하나 아니면 두개의 경우가 더 생길 가능성이 있음

        # 확인하고 맞으면 카운트 추가하고
        if last % expensive_price == 0:
            expensive_count += last//expensive_price
        else:
            # 아니면 원상복구
            cheap_count += 1
            last -= cheap_price

    print(f"#{tc} {cheap_count + expensive_count}")

N = int(input())

pack5 = N//5
rest = N % 5
pack3 = rest // 3
full_pack = pack5 * 5 + pack3 * 3
result = pack3 + pack5

while full_pack != N:
    # 5를 하나씩 깎으면서 진행
    pack5 = pack5 - 1
    rest = rest + 5
    pack3 = rest//3
    full_pack = pack5 * 5 + pack3 * 3

    if pack5 < 0:
        result = -1
        break

    if pack5 >= 0 and rest % 3 == 0:
        result = pack3+pack5
        break

print(result)

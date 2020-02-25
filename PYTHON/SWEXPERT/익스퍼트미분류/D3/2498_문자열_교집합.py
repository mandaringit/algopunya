T = int(input())

for tc in range(1, T + 1):
    a, b = map(int, input().split())
    set1 = set(input().split())
    set2 = set(input().split())
    print(f"#{tc}", len(set1 & set2))
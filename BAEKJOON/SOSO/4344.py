T = int(input())

for _ in range(T):
    inputs = list(map(int, input().split()))
    student_number = inputs[0]
    scores = inputs[1:]

    total = sum(scores)
    avg = total/student_number

    count = 0
    for score in scores:
        if score > avg:
            count += 1

    print(f"{count/student_number*100:.3f}%")

case_number = int(input())

for loop_number in range(case_number):
    word = input()
    output = f"#{loop_number + 1} "
    output = output + "1" if word == word[::-1] else output + "0"

    print(output)

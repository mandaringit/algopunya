total_number = int(input())
sorted_cases = sorted([int(number) for number in input().split()])
center_idx = total_number//2
print(sorted_cases[center_idx])

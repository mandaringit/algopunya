fixed_cost, change_cost, price = tuple(map(int, input().split()))

if price - change_cost <= 0:
    print("-1")
else:
    notebook = fixed_cost//(price - change_cost) + 1
    print(notebook)

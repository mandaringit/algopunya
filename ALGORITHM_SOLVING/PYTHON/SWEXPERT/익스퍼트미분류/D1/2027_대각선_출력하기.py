length = 5
for sharp in range(length):
    result = ""
    for plus in range(length):
        if plus == sharp:
            result += "#"
        else:
            result += "+"
    print(result)

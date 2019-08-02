
def type_inspect(argument):
    standard = 1
    if type(standard) != type(argument):
        raise ValueError

def calc_multiple (*args):
    result = 1
    try:
        for argument in args:
            type_inspect(argument)
            result *= argument

    except Exception:
        print("에러발생")
    else :
        print(result)

calc_multiple(1,2,3,4)


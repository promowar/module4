def divide(first, second):
    from math import inf
    if second > 0:
        x = first / second
    elif second == 0:
        x = inf
    return print(x)
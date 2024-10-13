data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]

kol = 0


def calculate(item):
    global kol
    if isinstance(item, int):
        kol += item
    elif isinstance(item, str):
        kol += len(item)
    elif isinstance(item, (list, tuple, set)):
        for i in item:
            calculate(i)
    elif isinstance(item, dict):
        for key, value in item.items():
            calculate(key)
            calculate(value)
    return kol


print(calculate(data_structure))

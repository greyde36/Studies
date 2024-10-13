g=[0,1,0]
h='0'
print(any(g), any(h))                           # если хотя бы 1 элемент True будет True, иначе False
print(all(g), all(h))                           # если все True будет True, иначе False
print(isinstance(g, str))                       # сравнение классов (True or False)
print(type(g)==str)                             # сравнение классов (True or False)

a = [1, 1, 1]
b = ''
d = [1, 1, 1]
c = d
c[0] = 2
print(c)
print(d)
print(id(a))
print(id(d))
print(id(c))
print(c is d)


def helper():
    """
    Эта функция-помощник
    """
    pass

print(helper.__doc__)                            # doc вызывает строку документирования
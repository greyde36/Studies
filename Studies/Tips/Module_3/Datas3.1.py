a = 5
b = 10


def printer():
#    global a, b                              # Присваивает значение переменой в глобал
    a = 'Str'
    b = 'Str2'
    c = 15
    d = 20
    print(a, d, c, d, 'Local')


printer()
print(a, b, 'Global')


    # lambda - не имеет имени, содержит 1 строку кода, при создании не используется def
result = lambda x, y: x+y
print(result(5,5))
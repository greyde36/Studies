def print_params(*, a=1, b=2, c=3):             # после "*" параметры указываются явно
     print(a, b, c)


print_params(c='string', a=2, b=True)


def func_with_params(a=2, b=2):
    print(a + b)
func_with_params(3, 3)                     # если не указаны "a,b" или им нужно дать новое значение
func_with_params(3)                              # если не указан первый параметр
func_with_params(b=1)                            # если надо указать явно параметр


def func_with_params1(a, b=2, c=[]):
    c.append(a)
    print(c)
func_with_params1(3)                             # список из функции не обнуляется, а дополняется
func_with_params1(3)
func_with_params1(3)


def func_with_params2(a, b=2, c=None):
    if c is None:
        c = []
        c.append(a)
    print(c)
func_with_params2(3)                             # "С" всегда неизвестно, поэтому список создаётся заново
func_with_params2(3)
func_with_params2(3)

txt='Нельзя отправлять письмо самому себе'
print(txt.endswith('льз',0,5))                   # Проверка на что заканчивается и диапазон
print(txt.endswith('льз','себе','бе'))           # True либо False, проверка на что заканчивается
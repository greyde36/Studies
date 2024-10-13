def say_hello():                                  # Обычная функция, количество вызовов не ограничено
    print('Hello')
say_hello()
#############################################################################################
def say_hello(name):                              # Принимающая функция
    print('Hello',name)
say_hello('Greyde')
say_hello('Max')
#############################################################################################
import random
def lottery():                                    # Возвращающая функция
    tickets = [1,2,3,4,5,6,7,8,9,10]
    win=random.choice(tickets)
    return win                                    # так же прекращает существование функции = break
win=lottery()
print(win)
#############################################################################################
def lottery(mon,thue):                            # Возвращающая, принимающая функция
    tickets = [1,2,3,4,5,6,7,8,9,10]
    win1=random.choice(tickets)
    tickets.remove(win1)
    win2=random.choice(tickets)
    print(mon,thue)
    return win1, win2
win1, win2 = lottery('mon','thue')
print(win1,win2)
#############################################################################################
def lottery(*args, **kwargs):                     # Возвращающая, принимающая функция
    tickets = [1,2,3,4,5,6,7,8,9,10]
    win1=random.choice(tickets)
    tickets.remove(win1)
    win2=random.choice(tickets)
    print(args)
    return win1, win2
win1, win2 = lottery(1,2,3,4,5)              # args = только цифры
print(win1,win2)                                   # kwargs =
#############################################################################################
def test(a=2, b=True):                             # Заданные принимающие функции
    print(a, b)
test(False,'ok')    #test()                  # если оставить пустые автозаполнение, при заполнение смена
#############################################################################################
def test(a=2, b=True):
    print(a, b)
test([1,2])                                        # [] заменяет первое условие функции
test(*[1,2])                                       # *[] заменяет оба условия функции
#test(**[1,2])                                     # **[] для распаковки словаря
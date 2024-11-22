# Простой декоратор
def null_decorator(func):
    return func
def greet():
    return 'Hello!'
greet=null_decorator(greet)             # Декоратор обязательно должен возвращать функцию
print(greet())                          # При данном способе функционал функции сохраняется
print("################Пример 2################")
# Можно использовать синтаксис Python @ для декодирования функции за один шаг
def null_decorator(func):
    return func
@null_decorator                         # При данном способе функция всегда будет декоратором
def greet():
    return 'Hello!'
print(greet())
print("################Пример 3################")
# Почему внутри декоратора нужно определить ещё одну функцию
def uppercase(func):
    def wrapper():
        original_result=func()
        modified_result=original_result.upper()
        return modified_result
    return wrapper
@uppercase
def greet():
    return 'Hello!'
print(greet())
print("################Пример 4################")
import time
import sys
def time_track(func):
    def surrogate(*args,**kwargs):
        started_at=time.time()
        result=func(*args,**kwargs)             # сохраняем результат функции digits
        ended_at=time.time()
        elapsed=round(ended_at-started_at,4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result                           # возвращает результат функции digits
    return surrogate
@time_track                                     # Дополнение функции новым условием (время выполнение работы)
def digits(*args):
    total=1
    for number in args:
        total *=number**5000
    return len(str(total))
sys.set_int_max_str_digits(100000)
result=digits(3141,5926,2718,2818)
print(result)
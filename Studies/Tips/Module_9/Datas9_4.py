# одноразовые функции без def (lambda), лямбда работает только 1 раз
my_func=lambda x: x+10
print(my_func(x=42))
print(type(my_func))
my_numbers=[3,1,4,1,5,9,2,6]
result=map(lambda x: x+10, my_numbers)          # в Х подставляет набор из my_numbers
print(list(result))
print('###################Пример 2########################')
# Лямбда может принимать несколько параметров или не одного
my_numbers=[3,1,4,1,5,9,2,6]
they_numbers=[2,7,1,8,2,8,1,8]
result2=map(lambda x,y: x+y, my_numbers, they_numbers)
print(list(result2))
# - Она создаётся в процессе выполнения кода и может просадить быстродействие
# - Она плохо сериализуется - могут быть проблемы в крупных фреймворках
# - Если в лямбде более 3-5 операторов лучше сделать def
print('###################Пример 3########################')
def get_multiplier_v1(n):
    if n==2:
        def multiplier(x):
            return x*2
    elif n==3:
        def multiplier(x):
            return x*3
    else:
        raise Exception('Я могу сделать умножители только на 2 и 3!')
    return multiplier
my_numbers=[3,1,4,1,5,9,2,6]
by_2=get_multiplier_v1(2)
by_3=get_multiplier_v1(3)

result3=map(by_2,my_numbers)
print(list(result3))
result3=map(by_3,my_numbers)
print(list(result3))
# get_multiplier_v1 - функция высшего порядка, она возвращает функции
print('###################Пример 4########################')
def get_multiplier_v2(n):
    def multiplier(x):
        return x*n
    return multiplier
by_5=get_multiplier_v2(5)           # замыкание переменной т.к сохранена функция внутри функции с возвратом на неё,
print(by_5(x=42))                   # параметр внешней функции остаётся в памяти(зафиксирован)
my_numbers=[3,1,4,1,5,9,2,6]
by_10=get_multiplier_v2(10)
by_100=get_multiplier_v2(100)
print(list(map(by_10,my_numbers)))
print(list(map(by_100,my_numbers)))
print('###################Пример 5########################')
from pprint import pprint
def matrix(some_list):
    def multiply_colum(x):
        res=[]
        for element in some_list:
            res.append(element*x)
        return res
    return multiply_colum
my_numbers=[3,1,4,1,5,9,2,6]
they_numbers=[2,7,1,8,2,8,1,8]
matrix_on_my_numbers=matrix(my_numbers)
result5=map(matrix_on_my_numbers, they_numbers)
pprint(list(result5))
my_numbers.extend([10,20,30])
result6=map(matrix_on_my_numbers, they_numbers)
pprint(list(result6))
print('###################Пример 6########################')
class Multiplier:
    def __init__(self,n):
        self.n=n
    def __call__(self, x):
        # если есть такой метод у класса - то его объект можно "вызывать" как функцию
        return x*self.n
my_numbers=[3,1,4,1,5,9,2,6]
by_100500=Multiplier(n=100500)
result7=by_100500(x=42)
print(result7)
result7=map(by_100500, my_numbers)
print(list(result7))
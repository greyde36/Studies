def get_russian_names():
    print(['Ваня', 'Коля', 'Маша'])
get_russian_names()
print(type(get_russian_names))
print(get_russian_names.__name__)
print('###########################################')
        #пример 2
def get_russian_names_2():
    return ['Ваня', 'Коля', 'Маша']
my_func = get_russian_names_2
print(my_func())
print(my_func.__name__)
print('###########################################')
        # пример 3 - с функцией можно работать как с обычными объектами
def get_russian_Names():
    return ['Ваня', 'Коля', 'Маша']
def get_british_Names():
    return ['Oliver', 'Jack', 'Harry']
name_gatters=[get_russian_Names,get_british_Names]
for name_gatter in name_gatters:
    print(name_gatter())
print('###########################################')
        # пример 4 - функции, принимающие на вход другие функции с аргументами
def adder(args):
    res=0
    for number in args:
        res+=number
    return res
def multiplier(args):
    res=1
    for number in args:
        res *= number
    return res
def process_numbers(numbers, function):
    result=function(numbers)
    print(f'Получилось {result}')
my_numbers=[3,1,4,1,5,9,2,6]
process_numbers(numbers=my_numbers,function=adder)
process_numbers(numbers=my_numbers,function=multiplier)
print('###########################################')
        # пример 5 - функция map
    # map применяет функцию к каждому элементу последовательности и формирует список результатов
def mul_by_2(x):
    return x*2
my_numbers=[3,1,4,1,5,9,2,6]
result=map(mul_by_2, my_numbers)            # 1 аргумент - функция, 2 аргумент - список
print(result)
print(list(result))
print('###########################################')
        # пример 6 - функция filter
    # filter вычисляет функцию для каждого элемента и добавляет элемент в список результатов,
    # если только функция вернула True тогда этот элемент остаётся в функции
def is_odd(x):
    return x%2
my_numbers=[3,1,4,1,5,9,2,6]
result1=filter(is_odd,my_numbers)           # где результат не =0 остались в списке (все число больше 0 True)
print(result1)
print(list(result1))
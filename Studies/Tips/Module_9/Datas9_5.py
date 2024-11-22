# Итератор использует ленивые вычисления (занимают мало памяти и экономят время)
import sys
from itertools import repeat
ex_itertator=repeat('4',100_000)                            # ленивое вычисление
print(ex_itertator)
print(f'Размер итератора - {sys.getsizeof(ex_itertator)}')
ex_str='4'*100_100                                          # вычисляет сразу (занимает много памяти)
print(f'Размер списка - {sys.getsizeof(ex_str)}')
print('###################Пример 2###################')
class Iter:
    def __init__(self):
        self.first='Первый элемент'
        self.second='Второй элемент'
        self.third='Третий элемент'
        self.i=0
    def __iter__(self):             # Получение итератора для перебора
        self.i=0                            # Обнуляем счётчик перед циклом
        return self                         # Возвращаем ссылку на себя, так как сам объект должен быть итератором
    def __next__(self):             # Переход к следующему значению
        # этот метод возвращает значения по требованию python (ленивые вычисления)
        self.i+=1
        if self.i==1:
            return self.first
        if self.i==2:
            return self.second
        if self.i==3:
            return self.third
        if self.i==4:
            return 'Подсчет закончен'
        raise StopIteration()               # признак того, что больше возвращать нечего
obj=Iter()
print(obj)
for value in obj:
    print(value)
# То есть интерпретатор вызывает метод __next__ при каждом проходе цикла
# Если в  __next__ возникает исключение StopIteration - то значение в объекте не больше, цикл прекращается
print('###################Пример 3###################')
try:
    while True:
        value=obj.__next__()
        print(value)
except StopIteration:
    print('Цикл for закончен')
print('###################Пример 4###################')
def fibonacci(n):                           # пример который занимает много памяти
    result=[]                               #   |
    a,b=0,1                                 #   |
    for _ in range(n):                      #   |
        result.append(a)                    #   |
        a,b=b,a+b                           #   |
    return result                           #   |
for value in fibonacci(n=10):               #   |
    print(value)                            #   |
print('######################################')
class Fibonacci:
    """Итератор последовательности Фибоначчи до N элементов"""
    def __init__(self,n):
        self.i, self.a, self.b, self.n=0,0,1,n
    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self
    def __next__(self):
        self.i+=1
        if self.i>1:
            if self.i>self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a
fib_iterator=Fibonacci(11)
print(fib_iterator)
for value in fib_iterator:
    print(value)
# Каждое число вычисляется "по месту" - тогда, когда оно понадобилось
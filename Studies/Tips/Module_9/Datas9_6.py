def func_generator(n):
    i = 0
    while i != n:
        yield i
        i += 1
obj = func_generator(10)
print(obj)
for i in obj:
    print(i)
print('###################Пример 2###################')
def fibonacci_v1(n):
    result=[]
    a,b=0,1
    for _ in range(n):
        result.append(a)                        # Хранит в себе список для выведения результата
        a,b=b, a+b                              # что занимает место в памяти
    return result
def fibonacci_v2(n):
    a,b=0,1
    for _ in range(n):
        yield a                                 # Возвращает результат, потом продолжает функцию
        a,b=b, a+b
fib_1=fibonacci_v1(n=10)
print(fib_1)
for value in fib_1:
    print(value)
fib_2=fibonacci_v2(n=10)                        # Генераторные сборки одноразовые
print(fib_2)
for value in fib_2:
    print(value)
print('###################Пример 3###################')
def fibonacci_v3():
    a,b=0,1
    while True:
        yield a
        a,b=b, a+b
for value in fibonacci_v3():
    print(value)
    if value>10**3:
        break
print('###################Пример 4###################')
import time
start=time.time()
def read_large_file(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        for line in file:
            yield line.strip()
for line in read_large_file("large_file.text"):
    print(line)
fin=time.time()
print((fin-start)*1000)
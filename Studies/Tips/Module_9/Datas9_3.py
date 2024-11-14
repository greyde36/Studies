# Пример 1 - ленивые вычисления - значения вычисляются при запросе (обычные вычисления делаются сразу, ленивые при их вызове)
my_numbers=[3,1,4,1,5,9,2,6]
result1=(x**100 for x in my_numbers)
print(result1)
for elem in result1:
    print(elem)
print('######################Пример 2#########################')
# Пример 2 - генераторные сборки можно прочитать только 1 раз
my_numbers=[3,1,4,1,5,9,2,6]
result2=(x**100 for x in my_numbers)
for elem in result2:
    print(elem)
print('Ещё разок')
for elem in result2:
    print(elem)
print('######################Пример 3#########################')
# Пример 3 - используются там где нужно производить затратные операции
import time
start_time=time.time()
my_numbers=[3,1,4,1,5,9,2,6]
result3=(x**3000 for x in my_numbers)
print(result3)
for i in result3:
    print(i)
finish_time=time.time()
print(f'Время в миллисекундах: {(finish_time-start_time)*1000}')
print('######################Пример 4#########################')
# Пример 4 - демонстрация встроенных функций с ленивыми вычислениями
list_1=[1,5,9,29,4]
list_2=[5,2,9,1,2]
ran=range(10,30)
zp=zip(list_1,list_2)
mp=map(str,list_1)
print(ran,zp,mp)
print(list(ran))
print(list(zp))
print(list(mp))
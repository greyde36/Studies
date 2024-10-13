food = ['apple', 'coconut', 'banana']                # Список (в списке могут храниться любые данные)
print(food[2])                                       # Выбор из списка (счёт начинается с 0)
food[2] = 'pineapple'
print(food)
food.append(True)                                    # Добавляет в конец списка
print(food)
food.extend('meet')                                  # Добавляет элемент разбитый на части по 1
food.extend('string'[2])                             # Добавляет 1 символ из объекта
print(food)
food.remove('e')                                     # Удаляет объект
print(food)
print('coconut' in food)                             # Находится ли этот объект в списке (True, False)
print('coconut' not in food)                         # Не находится ли этот объект в списке (True, False)
sentence = "Python is a popular programming language. Python is versatile and easy to learn."
count = sentence.count('Python')                     # Поиск слова и вывод количества повторений
print(count)  # Вывод: 2
print(food[2:5])                                     # Выбор по принципу строк
print(len(food))                                     # Количество символов в переменной
#####################################################################################################################
tuple_ =   1, 2, True, 'Meet'                           # Не
tuple_2 =  (1, 2, 3, 4 )                                #    изменяемые
tuple_3 = tuple([1, 2, 3, 4])                           #               элементы
print(tuple_)                                           # Кортеж
print(tuple_2[2])
print(tuple_3)
#tuple_ [0] = 36                                        # Не изменяемое
tuple_0 = ([1,2,3], 2)                                  # Внутри кортежа есть список, список изменяем
tuple_0 [0][0] = 8                                      # выбор списка, выбор из списка, присвоение
print(tuple_0)
print(tuple_0 + (3,3))                                  # Сложение кортежей
print(tuple_0 * 3)                                      # Умножение
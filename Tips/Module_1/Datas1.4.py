phone_book = {'Сергей': 4481080, 'Max': 5553535}             # Словарь, '' <- ключ (неизменяем)
print(phone_book)
print(phone_book['Max'])                                     # Вывести значение ключа
phone_book['Max'] = 5550000                                  # Замена значения у ключа
print(phone_book)
phone_book['Anton'] = 8888888                                # При отсутствии ключа в списке добавляет его
print(phone_book)
del phone_book['Anton']                                      # Удаление ключа из списка
print(phone_book)
phone_book.update({'Ser': 8968972, 'Alex': 9267583})         # Добавление к списку ещё список
print(phone_book)
print(phone_book.get('Max'))
print(phone_book.get('Rosa'))                                # При отсутствии ключа не добавляет его в список
print(phone_book.get('Rosa', 'Такого ключа нет'))            # Без ошибки выведет текст
phone_book.pop('Ser')                                        # Извлечение из словаря
print(phone_book)
a = phone_book.pop('Alex')                                   # Извлечение из словаря в переменную с присвоением
print(a)
list = [1,2,3]
list.pop(0)                                                  # удаление элемента
print(list)
print(phone_book.keys())                                     # список ключей в словаре
print(phone_book.values())                                   # список значений в словаре
print(phone_book.items())                                    # список ключей и значений в словаре
phone_book2 = {'Сер': [41080, 21421], 'Maxim': 55535}        # значений в ключе может быть несколько
print(phone_book2['Сер'][1])
#dict(zip('Max', 35))                                         # Добавление в архив (dict преобразование в словарь)
###########################################################################################################################################################################
set_ = {1,2,3,4,5,1,2,3,'String',True, (1,2,3)}              # Множество (хранит только уникальные значения)(не показывает повторы)
print(set_)
list_ = [1,1,1,2,3,4,2,2]
list_=set(list_)
print(list_)
# print(list_[0])                                             # Невозможно взять элемент из множества
print(list_.discard(1))                                       # Если нет элемента во множестве не выдаёт ошибку
print(list_)
print(list_.remove(2))                                        # Если нет Элемента во множестве, ошибка
print(list_)
print(list_.add(5))                                           # Добавить элемент
print(list_)
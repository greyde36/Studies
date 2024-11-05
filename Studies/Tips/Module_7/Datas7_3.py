import io
from pprint import pprint

name = 'sample3.txt'
file = open(name, 'r', encoding='utf-8')        # без encoding ошибка
print(file.writable())                          # файл открыт в режиме чтения и записывать в него нельзя (False)
print(file.readable())                          # файл открыт в режиме чтения и читать его можно (True)
print(file.seekable())                          # Есть ли возможно перемещать курсор (True)
print(file.tell())                              # подсчёт идёт в байтах
pprint(file.read())
print(file.tell())
file.close()
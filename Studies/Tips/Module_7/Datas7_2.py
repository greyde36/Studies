from pprint import pprint


name='sample.txt'
file=open(name, 'r')            # r, w, a  #r - read (чтение), w - write (запись), a - append (добавить)
pprint(file.read())
file.close()                    # ВСЕГДА файл нужно закрывать, могут быть потери, ошибки в коде


name='sample2.txt'
file=open(name, 'w')            # при каждом запуске записи файл перезаписывается чтобы, создать дубликат нужно
                                # переименовать файл, если такого не существует создаться новый
file.write('hello world!')
file.close()
file=open(name,'w')
file.write('vkycno i grystno((')    # перезапись
file.close()

file=open(name,'a')
file.write('\nAppend Text')     # Добавление к уже существующему
file.close()

print(file.tell())              # Показать, где находится курсор (он невидимый)
print(file.seek())              # Переместить курсор на Х позицию
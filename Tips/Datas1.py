name = 'Сергей'                             # - переменная
print('Hello'+name)                         # - сложение
print('Hello '+name)                        # - при "+" пробел не ставится автоматически
print('Hello',name)                         # - при "," пробел ставится автоматически
print('Hello '*5)                           # - при умножении слово повторяется
print(name[0])                              # - счёт начинается с 0, выбор буквы
print(name[-1])                             # - выбор с конца
print(name[0:3])                            # - выбор с 0 до 3
print(name[0:3:2])                          # - выбор с 0 до 3 каждая 2
print(name[:3])                             # - выбор от начала до 3
print(name[2:])                             # - выбор от 2 до конца
print(name[::-1])                           # - Реверс, написание наоборот
print(len(name))
name = 'sample4.txt'
with open(name, encoding='utf-8') as file:      # автоматически открывает в чтении
    for line in file:
        print(line, end='')                     # без end разрыв между строками
                                                # файл автоматически закрывается


print('')
name = 'sample4.txt'
with open(name, encoding='utf-8') as file:
    for line in file:
        for char in line:
            print(char)
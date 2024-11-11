def calc(line):
    operand_1, operation, operand_2 = line.split(' ')       # выбираем из текста всё что разделено пробелом
    operand_1 = int(operand_1)                              # перевод в целое число
    operand_2 = int(operand_2)
    if operation == '+':
        print(f'Результат:{operand_1 + operand_2}')         # Операция
    if operation == '-':
        print(f'Результат:{operand_1 - operand_2}')
    if operation == '/':
        print(f'Результат:{operand_1 / operand_2}')
    if operation == '//':
        print(f'Результат:{operand_1 // operand_2}')
    if operation == '%':
        print(f'Результат:{operand_1 % operand_2}')
    if operation == '*':
        print(f'Результат:{operand_1 * operand_2}')


cnt = 0                                                     # подсчёт строчек
with open('data.txt', 'r') as file:                         # Открыть текстовый файл и присвоить название file
    for line in file:                                       # выполнение функции для каждой строчки в файле
        cnt += 1
        try:
            calc(line)
        except ValueError as exc:                           # При возникновении ошибки ValueError
            if 'unpack' in exc.args[0]:             # Если в ошибке в 0 части кортежа есть слово "unpack" выполнять...
                print(f'Ошибка в линии {cnt}, не хватает данных для ответа')
            else:
                print(f'Ошибка в линии {cnt}, нельзя перевести в число')